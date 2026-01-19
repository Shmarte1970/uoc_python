"""
Menu Interactivo para OdontoCare
Sistema de Gestion de Citas Dentales

Este script permite interactuar con la API mediante un menu por consola
para realizar operaciones CRUD sobre doctores, pacientes, centros y citas.
"""
import requests
import json
from datetime import datetime, timedelta

# URLs de los servicios
URL_USUARIOS = "http://localhost:5001"
URL_CITAS = "http://localhost:5002"


class OdontoCareMenu:
    """Clase principal del menu interactivo"""

    def __init__(self):
        self.token = None
        self.headers = {'Content-Type': 'application/json'}
        self.usuario_actual = None

    # ==================== UTILIDADES ====================

    def limpiar_pantalla(self):
        """Imprime lineas para simular limpiar pantalla"""
        print("\n" * 2)

    def pausar(self):
        """Pausa hasta que el usuario presione Enter"""
        input("\nPresione ENTER para continuar...")

    def mostrar_error(self, mensaje):
        """Muestra un mensaje de error"""
        print(f"\n[ERROR] {mensaje}")

    def mostrar_exito(self, mensaje):
        """Muestra un mensaje de exito"""
        print(f"\n[OK] {mensaje}")

    def solicitar_dato(self, mensaje, obligatorio=True):
        """Solicita un dato al usuario"""
        while True:
            valor = input(f"{mensaje}: ").strip()
            if valor or not obligatorio:
                return valor
            print("Este campo es obligatorio. Intente nuevamente.")

    def solicitar_opcion(self, mensaje, opciones_validas):
        """Solicita una opcion valida al usuario"""
        while True:
            opcion = input(f"{mensaje}: ").strip()
            if opcion in opciones_validas:
                return opcion
            print(f"Opcion no valida. Opciones: {', '.join(opciones_validas)}")

    # ==================== AUTENTICACION ====================

    def login(self):
        """Realiza el login y obtiene el token"""
        print("\n" + "=" * 50)
        print("         INICIO DE SESION")
        print("=" * 50)

        username = self.solicitar_dato("Usuario")
        password = self.solicitar_dato("Contrasena")

        try:
            response = requests.post(
                f"{URL_USUARIOS}/auth/login",
                json={"username": username, "password": password},
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                self.token = data['token']
                self.headers['Authorization'] = f"Bearer {self.token}"
                self.usuario_actual = data['usuario']
                self.mostrar_exito(f"Bienvenido, {self.usuario_actual['username']} (Rol: {self.usuario_actual['rol']})")
                return True
            else:
                self.mostrar_error(response.json().get('error', 'Credenciales invalidas'))
                return False

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")
            print("\nAsegurese de que Docker esta corriendo:")
            print("  cd odontocare && docker-compose up -d")
            return False

    # ==================== MENU PRINCIPAL ====================

    def mostrar_menu_principal(self):
        """Muestra el menu principal"""
        print("\n" + "=" * 50)
        print("       ODONTOCARE - MENU PRINCIPAL")
        print("=" * 50)
        print(f"  Usuario: {self.usuario_actual['username']} ({self.usuario_actual['rol']})")
        print("-" * 50)
        print("  1. Gestion de Doctores")
        print("  2. Gestion de Pacientes")
        print("  3. Gestion de Centros Medicos")
        print("  4. Gestion de Citas")
        print("  5. Gestion de Usuarios")
        print("  6. Ver resumen del sistema")
        print("  0. Salir")
        print("-" * 50)

    # ==================== GESTION DE DOCTORES ====================

    def menu_doctores(self):
        """Menu de gestion de doctores"""
        while True:
            print("\n" + "=" * 50)
            print("       GESTION DE DOCTORES")
            print("=" * 50)
            print("  1. Listar todos los doctores")
            print("  2. Buscar doctor por ID")
            print("  3. Crear nuevo doctor")
            print("  4. Eliminar doctor")
            print("  0. Volver al menu principal")
            print("-" * 50)

            opcion = self.solicitar_opcion("Seleccione una opcion", ['0', '1', '2', '3', '4'])

            if opcion == '0':
                break
            elif opcion == '1':
                self.listar_doctores()
            elif opcion == '2':
                self.buscar_doctor()
            elif opcion == '3':
                self.crear_doctor()
            elif opcion == '4':
                self.eliminar_doctor()

    def listar_doctores(self):
        """Lista todos los doctores"""
        try:
            response = requests.get(
                f"{URL_USUARIOS}/admin/doctores",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                doctores = data.get('doctores', [])

                print("\n" + "-" * 85)
                print(f"{'ID':<6} {'NOMBRE':<40} {'ESPECIALIDAD':<35}")
                print("-" * 85)

                if doctores:
                    for d in doctores:
                        nombre = d['nombre'][:38] if len(d['nombre']) > 38 else d['nombre']
                        especialidad = d.get('especialidad', '-') or '-'
                        especialidad = especialidad[:33] if len(especialidad) > 33 else especialidad
                        print(f"{d['id_doctor']:<6} {nombre:<40} {especialidad:<35}")
                else:
                    print("  No hay doctores registrados")

                print("-" * 85)
                print(f"Total: {data.get('total', 0)} doctores")
            else:
                self.mostrar_error(response.json().get('error', 'Error al listar doctores'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def buscar_doctor(self):
        """Busca un doctor por ID"""
        id_doctor = self.solicitar_dato("Ingrese el ID del doctor")

        try:
            response = requests.get(
                f"{URL_USUARIOS}/admin/doctores/{id_doctor}",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                doctor = response.json()
                print("\n" + "-" * 40)
                print("DATOS DEL DOCTOR:")
                print("-" * 40)
                print(f"  ID:           {doctor['id_doctor']}")
                print(f"  Nombre:       {doctor['nombre']}")
                print(f"  Especialidad: {doctor.get('especialidad', '-')}")
                print(f"  ID Usuario:   {doctor.get('id_usuario', '-')}")
                print("-" * 40)
            else:
                self.mostrar_error(response.json().get('error', 'Doctor no encontrado'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def crear_doctor(self):
        """Crea un nuevo doctor"""
        print("\n--- CREAR NUEVO DOCTOR ---\n")

        nombre = self.solicitar_dato("Nombre completo")
        especialidad = self.solicitar_dato("Especialidad", obligatorio=False)

        crear_usuario = self.solicitar_opcion("Crear usuario de acceso? (s/n)", ['s', 'n'])

        data = {
            "nombre": nombre,
            "especialidad": especialidad
        }

        if crear_usuario == 's':
            data["username"] = self.solicitar_dato("Username para el doctor")
            data["password"] = self.solicitar_dato("Password")

        try:
            response = requests.post(
                f"{URL_USUARIOS}/admin/doctores",
                json=data,
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 201:
                doctor = response.json()['doctor']
                self.mostrar_exito(f"Doctor creado con ID: {doctor['id_doctor']}")
            else:
                self.mostrar_error(response.json().get('error', 'Error al crear doctor'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def eliminar_doctor(self):
        """Elimina un doctor"""
        self.listar_doctores()
        id_doctor = self.solicitar_dato("Ingrese el ID del doctor a eliminar")

        confirmar = self.solicitar_opcion(f"Confirmar eliminacion del doctor {id_doctor}? (s/n)", ['s', 'n'])

        if confirmar == 's':
            try:
                response = requests.delete(
                    f"{URL_USUARIOS}/admin/doctores/{id_doctor}",
                    headers=self.headers,
                    timeout=10
                )

                if response.status_code == 200:
                    self.mostrar_exito("Doctor eliminado correctamente")
                else:
                    self.mostrar_error(response.json().get('error', 'Error al eliminar doctor'))

            except requests.RequestException as e:
                self.mostrar_error(f"Error de conexion: {e}")
        else:
            print("Operacion cancelada")

        self.pausar()

    # ==================== GESTION DE PACIENTES ====================

    def menu_pacientes(self):
        """Menu de gestion de pacientes"""
        while True:
            print("\n" + "=" * 50)
            print("       GESTION DE PACIENTES")
            print("=" * 50)
            print("  1. Listar todos los pacientes")
            print("  2. Buscar paciente por ID")
            print("  3. Crear nuevo paciente")
            print("  4. Modificar estado del paciente")
            print("  5. Eliminar paciente")
            print("  0. Volver al menu principal")
            print("-" * 50)

            opcion = self.solicitar_opcion("Seleccione una opcion", ['0', '1', '2', '3', '4', '5'])

            if opcion == '0':
                break
            elif opcion == '1':
                self.listar_pacientes()
            elif opcion == '2':
                self.buscar_paciente()
            elif opcion == '3':
                self.crear_paciente()
            elif opcion == '4':
                self.modificar_estado_paciente()
            elif opcion == '5':
                self.eliminar_paciente()

    def listar_pacientes(self):
        """Lista todos los pacientes"""
        try:
            response = requests.get(
                f"{URL_USUARIOS}/admin/pacientes",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                pacientes = data.get('pacientes', [])

                print("\n" + "-" * 85)
                print(f"{'ID':<6} {'NOMBRE':<40} {'TELEFONO':<15} {'ESTADO':<12}")
                print("-" * 85)

                if pacientes:
                    for p in pacientes:
                        nombre = p['nombre'][:38] if len(p['nombre']) > 38 else p['nombre']
                        print(f"{p['id_paciente']:<6} {nombre:<40} {p.get('telefono', '-'):<15} {p.get('estado', '-'):<12}")
                else:
                    print("  No hay pacientes registrados")

                print("-" * 85)
                print(f"Total: {data.get('total', 0)} pacientes")
            else:
                self.mostrar_error(response.json().get('error', 'Error al listar pacientes'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def buscar_paciente(self):
        """Busca un paciente por ID"""
        id_paciente = self.solicitar_dato("Ingrese el ID del paciente")

        try:
            response = requests.get(
                f"{URL_USUARIOS}/admin/pacientes/{id_paciente}",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                paciente = response.json()
                print("\n" + "-" * 40)
                print("DATOS DEL PACIENTE:")
                print("-" * 40)
                print(f"  ID:        {paciente['id_paciente']}")
                print(f"  Nombre:    {paciente['nombre']}")
                print(f"  Telefono:  {paciente.get('telefono', '-')}")
                print(f"  Estado:    {paciente.get('estado', '-')}")
                print(f"  ID Usuario:{paciente.get('id_usuario', '-')}")
                print("-" * 40)
            else:
                self.mostrar_error(response.json().get('error', 'Paciente no encontrado'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def crear_paciente(self):
        """Crea un nuevo paciente"""
        print("\n--- CREAR NUEVO PACIENTE ---\n")

        nombre = self.solicitar_dato("Nombre completo")
        telefono = self.solicitar_dato("Telefono", obligatorio=False)

        # Estado con opciones numericas para evitar errores
        estado_opcion = self.solicitar_opcion("Estado (1-ACTIVO / 0-INACTIVO)", ['1', '0'])
        estado = "ACTIVO" if estado_opcion == '1' else "INACTIVO"

        data = {
            "nombre": nombre,
            "telefono": telefono,
            "estado": estado
        }

        try:
            response = requests.post(
                f"{URL_USUARIOS}/admin/pacientes",
                json=data,
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 201:
                paciente = response.json()['paciente']
                self.mostrar_exito(f"Paciente creado con ID: {paciente['id_paciente']}")
            else:
                self.mostrar_error(response.json().get('error', 'Error al crear paciente'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def modificar_estado_paciente(self):
        """Modifica el estado de un paciente"""
        self.listar_pacientes()
        id_paciente = self.solicitar_dato("Ingrese el ID del paciente a modificar")

        # Estado con opciones numericas para evitar errores
        estado_opcion = self.solicitar_opcion("Nuevo estado (1-ACTIVO / 0-INACTIVO)", ['1', '0'])
        nuevo_estado = "ACTIVO" if estado_opcion == '1' else "INACTIVO"

        try:
            response = requests.put(
                f"{URL_USUARIOS}/admin/pacientes/{id_paciente}",
                json={"estado": nuevo_estado},
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                self.mostrar_exito(f"Estado actualizado a {nuevo_estado}")
            else:
                self.mostrar_error(response.json().get('error', 'Error al modificar paciente'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def eliminar_paciente(self):
        """Elimina un paciente"""
        self.listar_pacientes()
        id_paciente = self.solicitar_dato("Ingrese el ID del paciente a eliminar")

        confirmar = self.solicitar_opcion(f"Confirmar eliminacion del paciente {id_paciente}? (s/n)", ['s', 'n'])

        if confirmar == 's':
            try:
                response = requests.delete(
                    f"{URL_USUARIOS}/admin/pacientes/{id_paciente}",
                    headers=self.headers,
                    timeout=10
                )

                if response.status_code == 200:
                    self.mostrar_exito("Paciente eliminado correctamente")
                else:
                    self.mostrar_error(response.json().get('error', 'Error al eliminar paciente'))

            except requests.RequestException as e:
                self.mostrar_error(f"Error de conexion: {e}")
        else:
            print("Operacion cancelada")

        self.pausar()

    # ==================== GESTION DE CENTROS ====================

    def menu_centros(self):
        """Menu de gestion de centros medicos"""
        while True:
            print("\n" + "=" * 50)
            print("       GESTION DE CENTROS MEDICOS")
            print("=" * 50)
            print("  1. Listar todos los centros")
            print("  2. Buscar centro por ID")
            print("  3. Crear nuevo centro")
            print("  4. Eliminar centro")
            print("  0. Volver al menu principal")
            print("-" * 50)

            opcion = self.solicitar_opcion("Seleccione una opcion", ['0', '1', '2', '3', '4'])

            if opcion == '0':
                break
            elif opcion == '1':
                self.listar_centros()
            elif opcion == '2':
                self.buscar_centro()
            elif opcion == '3':
                self.crear_centro()
            elif opcion == '4':
                self.eliminar_centro()

    def listar_centros(self):
        """Lista todos los centros"""
        try:
            response = requests.get(
                f"{URL_USUARIOS}/admin/centros",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                centros = data.get('centros', [])

                print("\n" + "-" * 110)
                print(f"{'ID':<6} {'NOMBRE':<45} {'DIRECCION':<55}")
                print("-" * 110)

                if centros:
                    for c in centros:
                        nombre = c['nombre'][:43] if len(c['nombre']) > 43 else c['nombre']
                        direccion = c.get('direccion', '-') or '-'
                        direccion = direccion[:53] if len(direccion) > 53 else direccion
                        print(f"{c['id_centro']:<6} {nombre:<45} {direccion:<55}")
                else:
                    print("  No hay centros registrados")

                print("-" * 110)
                print(f"Total: {data.get('total', 0)} centros")
            else:
                self.mostrar_error(response.json().get('error', 'Error al listar centros'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def buscar_centro(self):
        """Busca un centro por ID"""
        id_centro = self.solicitar_dato("Ingrese el ID del centro")

        try:
            response = requests.get(
                f"{URL_USUARIOS}/admin/centros/{id_centro}",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                centro = response.json()
                print("\n" + "-" * 40)
                print("DATOS DEL CENTRO:")
                print("-" * 40)
                print(f"  ID:        {centro['id_centro']}")
                print(f"  Nombre:    {centro['nombre']}")
                print(f"  Direccion: {centro.get('direccion', '-')}")
                print("-" * 40)
            else:
                self.mostrar_error(response.json().get('error', 'Centro no encontrado'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def crear_centro(self):
        """Crea un nuevo centro"""
        print("\n--- CREAR NUEVO CENTRO ---\n")

        nombre = self.solicitar_dato("Nombre del centro")
        direccion = self.solicitar_dato("Direccion", obligatorio=False)

        try:
            response = requests.post(
                f"{URL_USUARIOS}/admin/centros",
                json={"nombre": nombre, "direccion": direccion},
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 201:
                centro = response.json()['centro']
                self.mostrar_exito(f"Centro creado con ID: {centro['id_centro']}")
            else:
                self.mostrar_error(response.json().get('error', 'Error al crear centro'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def eliminar_centro(self):
        """Elimina un centro"""
        self.listar_centros()
        id_centro = self.solicitar_dato("Ingrese el ID del centro a eliminar")

        confirmar = self.solicitar_opcion(f"Confirmar eliminacion del centro {id_centro}? (s/n)", ['s', 'n'])

        if confirmar == 's':
            try:
                response = requests.delete(
                    f"{URL_USUARIOS}/admin/centros/{id_centro}",
                    headers=self.headers,
                    timeout=10
                )

                if response.status_code == 200:
                    self.mostrar_exito("Centro eliminado correctamente")
                else:
                    self.mostrar_error(response.json().get('error', 'Error al eliminar centro'))

            except requests.RequestException as e:
                self.mostrar_error(f"Error de conexion: {e}")
        else:
            print("Operacion cancelada")

        self.pausar()

    # ==================== GESTION DE CITAS ====================

    def menu_citas(self):
        """Menu de gestion de citas"""
        while True:
            print("\n" + "=" * 50)
            print("       GESTION DE CITAS MEDICAS")
            print("=" * 50)
            print("  1. Listar todas las citas")
            print("  2. Buscar cita por ID")
            print("  3. Crear nueva cita")
            print("  4. Cancelar cita")
            print("  5. Ver disponibilidad de doctor")
            print("  0. Volver al menu principal")
            print("-" * 50)

            opcion = self.solicitar_opcion("Seleccione una opcion", ['0', '1', '2', '3', '4', '5'])

            if opcion == '0':
                break
            elif opcion == '1':
                self.listar_citas()
            elif opcion == '2':
                self.buscar_cita()
            elif opcion == '3':
                self.crear_cita()
            elif opcion == '4':
                self.cancelar_cita()
            elif opcion == '5':
                self.ver_disponibilidad()

    def listar_citas(self):
        """Lista todas las citas"""
        try:
            response = requests.get(
                f"{URL_CITAS}/citas",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                citas = data.get('citas', [])

                print("\n" + "-" * 90)
                print(f"{'ID':<6} {'FECHA':<20} {'PACIENTE':<10} {'DOCTOR':<10} {'CENTRO':<10} {'ESTADO':<12} {'MOTIVO':<15}")
                print("-" * 90)

                if citas:
                    for c in citas:
                        fecha = c.get('fecha', '-')[:16] if c.get('fecha') else '-'
                        print(f"{c['id_cita']:<6} {fecha:<20} {c['id_paciente']:<10} {c['id_doctor']:<10} {c['id_centro']:<10} {c.get('estado', '-'):<12} {(c.get('motivo', '-') or '-')[:15]:<15}")
                else:
                    print("  No hay citas registradas")

                print("-" * 90)
                print(f"Total: {data.get('total', 0)} citas")
            else:
                self.mostrar_error(response.json().get('error', 'Error al listar citas'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def buscar_cita(self):
        """Busca una cita por ID"""
        id_cita = self.solicitar_dato("Ingrese el ID de la cita")

        try:
            response = requests.get(
                f"{URL_CITAS}/citas/{id_cita}",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                cita = response.json()
                print("\n" + "-" * 40)
                print("DATOS DE LA CITA:")
                print("-" * 40)
                print(f"  ID Cita:     {cita['id_cita']}")
                print(f"  Fecha:       {cita.get('fecha', '-')}")
                print(f"  Motivo:      {cita.get('motivo', '-')}")
                print(f"  Estado:      {cita.get('estado', '-')}")
                print(f"  ID Paciente: {cita['id_paciente']}")
                print(f"  ID Doctor:   {cita['id_doctor']}")
                print(f"  ID Centro:   {cita['id_centro']}")
                print("-" * 40)
            else:
                self.mostrar_error(response.json().get('error', 'Cita no encontrada'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def crear_cita(self):
        """Crea una nueva cita"""
        print("\n--- CREAR NUEVA CITA ---\n")

        # Mostrar pacientes disponibles
        print("PACIENTES DISPONIBLES:")
        try:
            resp = requests.get(f"{URL_USUARIOS}/admin/pacientes", headers=self.headers, timeout=10)
            if resp.status_code == 200:
                for p in resp.json().get('pacientes', []):
                    estado_marca = "[ACTIVO]" if p.get('estado') == 'ACTIVO' else "[INACTIVO]"
                    print(f"  {p['id_paciente']} - {p['nombre']} {estado_marca}")
        except:
            pass

        id_paciente = self.solicitar_dato("\nID del paciente")

        # Mostrar doctores disponibles
        print("\nDOCTORES DISPONIBLES:")
        try:
            resp = requests.get(f"{URL_USUARIOS}/admin/doctores", headers=self.headers, timeout=10)
            if resp.status_code == 200:
                for d in resp.json().get('doctores', []):
                    print(f"  {d['id_doctor']} - {d['nombre']} ({d.get('especialidad', '-')})")
        except:
            pass

        id_doctor = self.solicitar_dato("\nID del doctor")

        # Mostrar centros disponibles
        print("\nCENTROS DISPONIBLES:")
        try:
            resp = requests.get(f"{URL_USUARIOS}/admin/centros", headers=self.headers, timeout=10)
            if resp.status_code == 200:
                for c in resp.json().get('centros', []):
                    print(f"  {c['id_centro']} - {c['nombre']}")
        except:
            pass

        id_centro = self.solicitar_dato("\nID del centro")

        # Solicitar fecha
        print("\nFORMATO DE FECHA: YYYY-MM-DD HH:MM")
        print("Ejemplo: 2025-01-20 10:00")
        fecha_str = self.solicitar_dato("Fecha y hora de la cita")

        # Convertir a formato ISO
        try:
            fecha_dt = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
            fecha_iso = fecha_dt.isoformat()
        except ValueError:
            self.mostrar_error("Formato de fecha invalido")
            self.pausar()
            return

        motivo = self.solicitar_dato("Motivo de la cita", obligatorio=False)

        # Crear la cita
        try:
            response = requests.post(
                f"{URL_CITAS}/citas",
                json={
                    "id_paciente": int(id_paciente),
                    "id_doctor": int(id_doctor),
                    "id_centro": int(id_centro),
                    "fecha": fecha_iso,
                    "motivo": motivo
                },
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 201:
                cita = response.json()['cita']
                self.mostrar_exito(f"Cita creada con ID: {cita['id_cita']}")
                print("\nDetalles de la cita:")
                print(json.dumps(cita, indent=2, ensure_ascii=False))
            else:
                self.mostrar_error(response.json().get('error', 'Error al crear cita'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")
        except ValueError:
            self.mostrar_error("IDs deben ser numeros")

        self.pausar()

    def cancelar_cita(self):
        """Cancela una cita"""
        self.listar_citas()
        id_cita = self.solicitar_dato("Ingrese el ID de la cita a cancelar")

        confirmar = self.solicitar_opcion(f"Confirmar cancelacion de la cita {id_cita}? (s/n)", ['s', 'n'])

        if confirmar == 's':
            try:
                response = requests.put(
                    f"{URL_CITAS}/citas/{id_cita}",
                    json={"estado": "CANCELADA"},
                    headers=self.headers,
                    timeout=10
                )

                if response.status_code == 200:
                    self.mostrar_exito("Cita cancelada correctamente")
                else:
                    self.mostrar_error(response.json().get('error', 'Error al cancelar cita'))

            except requests.RequestException as e:
                self.mostrar_error(f"Error de conexion: {e}")
        else:
            print("Operacion cancelada")

        self.pausar()

    def ver_disponibilidad(self):
        """Ver disponibilidad de un doctor en una fecha"""
        # Mostrar doctores
        print("\nDOCTORES DISPONIBLES:")
        try:
            resp = requests.get(f"{URL_USUARIOS}/admin/doctores", headers=self.headers, timeout=10)
            if resp.status_code == 200:
                for d in resp.json().get('doctores', []):
                    print(f"  {d['id_doctor']} - {d['nombre']}")
        except:
            pass

        id_doctor = self.solicitar_dato("\nID del doctor")
        fecha = self.solicitar_dato("Fecha a consultar (YYYY-MM-DD)")

        try:
            response = requests.get(
                f"{URL_CITAS}/citas/doctor/{id_doctor}/disponibilidad",
                params={"fecha": fecha},
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                print("\n" + "-" * 40)
                print(f"DISPONIBILIDAD - Doctor ID: {data['id_doctor']}")
                print(f"Fecha: {data['fecha']}")
                print("-" * 40)

                if data.get('horas_ocupadas'):
                    print("Horas ocupadas:")
                    for hora in data['horas_ocupadas']:
                        print(f"  - {hora}")
                else:
                    print("No tiene citas programadas para esta fecha")

                print(f"\nTotal citas del dia: {data.get('total_citas', 0)}")
                print("-" * 40)
            else:
                self.mostrar_error(response.json().get('error', 'Error al consultar disponibilidad'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    # ==================== GESTION DE USUARIOS ====================

    def menu_usuarios(self):
        """Menu de gestion de usuarios"""
        while True:
            print("\n" + "=" * 50)
            print("       GESTION DE USUARIOS")
            print("=" * 50)
            print("  1. Listar todos los usuarios")
            print("  2. Crear nuevo usuario (admin/secretaria)")
            print("  3. Eliminar usuario")
            print("  0. Volver al menu principal")
            print("-" * 50)

            opcion = self.solicitar_opcion("Seleccione una opcion", ['0', '1', '2', '3'])

            if opcion == '0':
                break
            elif opcion == '1':
                self.listar_usuarios()
            elif opcion == '2':
                self.crear_usuario()
            elif opcion == '3':
                self.eliminar_usuario()

    def listar_usuarios(self):
        """Lista todos los usuarios"""
        try:
            response = requests.get(
                f"{URL_USUARIOS}/admin/usuarios",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                usuarios = data.get('usuarios', [])

                print("\n" + "-" * 70)
                print(f"{'ID':<6} {'USERNAME':<25} {'ROL':<15}")
                print("-" * 70)

                if usuarios:
                    for u in usuarios:
                        username = u['username'][:23] if len(u['username']) > 23 else u['username']
                        print(f"{u['id_usuario']:<6} {username:<25} {u.get('rol', '-'):<15}")
                else:
                    print("  No hay usuarios registrados")

                print("-" * 70)
                print(f"Total: {data.get('total', 0)} usuarios")
            else:
                self.mostrar_error(response.json().get('error', 'Error al listar usuarios'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def crear_usuario(self):
        """Crea un nuevo usuario (admin o secretaria)"""
        print("\n--- CREAR NUEVO USUARIO ---\n")

        username = self.solicitar_dato("Username")
        password = self.solicitar_dato("Password")

        # Rol con opciones numericas
        print("\nRoles disponibles:")
        print("  1 - admin")
        print("  2 - secretaria")
        rol_opcion = self.solicitar_opcion("Seleccione rol (1/2)", ['1', '2'])
        rol = "admin" if rol_opcion == '1' else "secretaria"

        try:
            response = requests.post(
                f"{URL_USUARIOS}/admin/usuario",
                json={
                    "username": username,
                    "password": password,
                    "rol": rol
                },
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 201:
                usuario = response.json()['usuario']
                self.mostrar_exito(f"Usuario creado con ID: {usuario['id_usuario']}")
                print(f"  Username: {usuario['username']}")
                print(f"  Rol: {usuario['rol']}")
            else:
                self.mostrar_error(response.json().get('error', 'Error al crear usuario'))

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    def eliminar_usuario(self):
        """Elimina un usuario"""
        self.listar_usuarios()
        id_usuario = self.solicitar_dato("Ingrese el ID del usuario a eliminar")

        # Validar que no se elimine a si mismo
        if self.usuario_actual and str(self.usuario_actual.get('id_usuario')) == id_usuario:
            self.mostrar_error("No puede eliminar su propio usuario")
            self.pausar()
            return

        confirmar = self.solicitar_opcion(f"Confirmar eliminacion del usuario {id_usuario}? (s/n)", ['s', 'n'])

        if confirmar == 's':
            try:
                response = requests.delete(
                    f"{URL_USUARIOS}/admin/usuarios/{id_usuario}",
                    headers=self.headers,
                    timeout=10
                )

                if response.status_code == 200:
                    self.mostrar_exito("Usuario eliminado correctamente")
                else:
                    self.mostrar_error(response.json().get('error', 'Error al eliminar usuario'))

            except requests.RequestException as e:
                self.mostrar_error(f"Error de conexion: {e}")
        else:
            print("Operacion cancelada")

        self.pausar()

    # ==================== RESUMEN ====================

    def ver_resumen(self):
        """Muestra un resumen del sistema"""
        print("\n" + "=" * 50)
        print("       RESUMEN DEL SISTEMA")
        print("=" * 50)

        try:
            # Contar doctores
            resp = requests.get(f"{URL_USUARIOS}/admin/doctores", headers=self.headers, timeout=10)
            total_doctores = resp.json().get('total', 0) if resp.status_code == 200 else 'Error'

            # Contar pacientes
            resp = requests.get(f"{URL_USUARIOS}/admin/pacientes", headers=self.headers, timeout=10)
            total_pacientes = resp.json().get('total', 0) if resp.status_code == 200 else 'Error'

            # Contar centros
            resp = requests.get(f"{URL_USUARIOS}/admin/centros", headers=self.headers, timeout=10)
            total_centros = resp.json().get('total', 0) if resp.status_code == 200 else 'Error'

            # Contar citas
            resp = requests.get(f"{URL_CITAS}/citas", headers=self.headers, timeout=10)
            total_citas = resp.json().get('total', 0) if resp.status_code == 200 else 'Error'

            print(f"\n  Doctores registrados:  {total_doctores}")
            print(f"  Pacientes registrados: {total_pacientes}")
            print(f"  Centros medicos:       {total_centros}")
            print(f"  Citas totales:         {total_citas}")
            print("\n" + "=" * 50)

        except requests.RequestException as e:
            self.mostrar_error(f"Error de conexion: {e}")

        self.pausar()

    # ==================== EJECUCION PRINCIPAL ====================

    def ejecutar(self):
        """Ejecuta el menu principal"""
        print("\n" + "=" * 50)
        print("       ODONTOCARE")
        print("   Sistema de Gestion de Citas Dentales")
        print("=" * 50)

        # Login
        intentos = 0
        while intentos < 3:
            if self.login():
                break
            intentos += 1
            if intentos < 3:
                print(f"\nIntentos restantes: {3 - intentos}")
        else:
            print("\nDemasiados intentos fallidos. Saliendo...")
            return

        # Menu principal
        while True:
            self.mostrar_menu_principal()
            opcion = self.solicitar_opcion("Seleccione una opcion", ['0', '1', '2', '3', '4', '5', '6'])

            if opcion == '0':
                print("\nGracias por usar OdontoCare. Hasta pronto!")
                break
            elif opcion == '1':
                self.menu_doctores()
            elif opcion == '2':
                self.menu_pacientes()
            elif opcion == '3':
                self.menu_centros()
            elif opcion == '4':
                self.menu_citas()
            elif opcion == '5':
                self.menu_usuarios()
            elif opcion == '6':
                self.ver_resumen()


if __name__ == "__main__":
    menu = OdontoCareMenu()
    menu.ejecutar()
