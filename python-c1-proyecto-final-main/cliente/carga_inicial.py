"""
Cliente Python para OdontoCare
Script de carga inicial de datos y demostración de la API

Este script:
1. Realiza login con usuario admin
2. Procesa y envía los registros del archivo datos.csv
3. Crea una cita médica
4. Imprime en consola el JSON con la cita creada
"""
import csv
import requests
import json
from datetime import datetime, timedelta

# Configuración de URLs de los servicios
SERVICIO_USUARIOS_URL = "http://localhost:5001"
SERVICIO_CITAS_URL = "http://localhost:5002"

# Ruta al archivo CSV
CSV_FILE = "../data/datos.csv"


class OdontoCareClient:
    """Cliente para interactuar con la API de OdontoCare"""

    def __init__(self):
        self.token = None
        self.headers = {'Content-Type': 'application/json'}

    def login(self, username, password):
        """
        Realiza login y obtiene el token JWT

        Args:
            username: Nombre de usuario
            password: Contraseña

        Returns:
            bool: True si el login fue exitoso
        """
        print(f"\n{'='*50}")
        print(f"Iniciando sesión como: {username}")
        print('='*50)

        url = f"{SERVICIO_USUARIOS_URL}/auth/login"
        data = {"username": username, "password": password}

        try:
            response = requests.post(url, json=data, timeout=10)

            if response.status_code == 200:
                result = response.json()
                self.token = result['token']
                self.headers['Authorization'] = f"Bearer {self.token}"
                print(f"✓ Login exitoso")
                print(f"  Usuario: {result['usuario']['username']}")
                print(f"  Rol: {result['usuario']['rol']}")
                return True
            else:
                print(f"✗ Error en login: {response.json()}")
                return False

        except requests.RequestException as e:
            print(f"✗ Error de conexión: {e}")
            return False

    def crear_doctor(self, nombre, especialidad, username, password):
        """Crea un doctor en el sistema"""
        url = f"{SERVICIO_USUARIOS_URL}/admin/doctores"
        data = {
            "nombre": nombre,
            "especialidad": especialidad,
            "username": username,
            "password": password
        }

        try:
            response = requests.post(url, json=data, headers=self.headers, timeout=10)

            if response.status_code == 201:
                result = response.json()
                print(f"  ✓ Doctor creado: {nombre} ({especialidad})")
                return result['doctor']
            else:
                print(f"  ✗ Error creando doctor {nombre}: {response.json().get('error', 'Error desconocido')}")
                return None

        except requests.RequestException as e:
            print(f"  ✗ Error de conexión: {e}")
            return None

    def crear_paciente(self, nombre, telefono, username, password, estado='ACTIVO'):
        """Crea un paciente en el sistema"""
        url = f"{SERVICIO_USUARIOS_URL}/admin/pacientes"
        data = {
            "nombre": nombre,
            "telefono": telefono,
            "username": username,
            "password": password,
            "estado": estado
        }

        try:
            response = requests.post(url, json=data, headers=self.headers, timeout=10)

            if response.status_code == 201:
                result = response.json()
                print(f"  ✓ Paciente creado: {nombre}")
                return result['paciente']
            else:
                print(f"  ✗ Error creando paciente {nombre}: {response.json().get('error', 'Error desconocido')}")
                return None

        except requests.RequestException as e:
            print(f"  ✗ Error de conexión: {e}")
            return None

    def crear_centro(self, nombre, direccion):
        """Crea un centro médico en el sistema"""
        url = f"{SERVICIO_USUARIOS_URL}/admin/centros"
        data = {
            "nombre": nombre,
            "direccion": direccion
        }

        try:
            response = requests.post(url, json=data, headers=self.headers, timeout=10)

            if response.status_code == 201:
                result = response.json()
                print(f"  ✓ Centro creado: {nombre}")
                return result['centro']
            else:
                print(f"  ✗ Error creando centro {nombre}: {response.json().get('error', 'Error desconocido')}")
                return None

        except requests.RequestException as e:
            print(f"  ✗ Error de conexión: {e}")
            return None

    def crear_cita(self, id_paciente, id_doctor, id_centro, fecha, motivo):
        """Crea una cita médica en el sistema"""
        url = f"{SERVICIO_CITAS_URL}/citas"
        data = {
            "id_paciente": id_paciente,
            "id_doctor": id_doctor,
            "id_centro": id_centro,
            "fecha": fecha,
            "motivo": motivo
        }

        try:
            response = requests.post(url, json=data, headers=self.headers, timeout=10)

            if response.status_code == 201:
                result = response.json()
                print(f"  ✓ Cita creada exitosamente")
                return result['cita']
            else:
                print(f"  ✗ Error creando cita: {response.json().get('error', 'Error desconocido')}")
                return None

        except requests.RequestException as e:
            print(f"  ✗ Error de conexión: {e}")
            return None

    def listar_doctores(self):
        """Lista todos los doctores"""
        url = f"{SERVICIO_USUARIOS_URL}/admin/doctores"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException:
            return None

    def listar_pacientes(self):
        """Lista todos los pacientes"""
        url = f"{SERVICIO_USUARIOS_URL}/admin/pacientes"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException:
            return None

    def listar_centros(self):
        """Lista todos los centros"""
        url = f"{SERVICIO_USUARIOS_URL}/admin/centros"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException:
            return None

    def listar_citas(self):
        """Lista todas las citas"""
        url = f"{SERVICIO_CITAS_URL}/citas"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException:
            return None


def cargar_datos_csv(cliente, csv_path):
    """
    Carga los datos desde el archivo CSV

    Args:
        cliente: Instancia de OdontoCareClient
        csv_path: Ruta al archivo CSV
    """
    print(f"\n{'='*50}")
    print("Cargando datos desde CSV")
    print('='*50)

    doctores_creados = []
    pacientes_creados = []
    centros_creados = []

    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                tipo = row['tipo'].strip()

                if tipo == 'doctor':
                    doctor = cliente.crear_doctor(
                        nombre=row['nombre'].strip(),
                        especialidad=row['especialidad'].strip(),
                        username=row['username'].strip(),
                        password=row['password'].strip()
                    )
                    if doctor:
                        doctores_creados.append(doctor)

                elif tipo == 'paciente':
                    paciente = cliente.crear_paciente(
                        nombre=row['nombre'].strip(),
                        telefono=row['telefono'].strip(),
                        username=row['username'].strip(),
                        password=row['password'].strip(),
                        estado=row['estado'].strip() if row['estado'] else 'ACTIVO'
                    )
                    if paciente:
                        pacientes_creados.append(paciente)

                elif tipo == 'centro':
                    centro = cliente.crear_centro(
                        nombre=row['nombre'].strip(),
                        direccion=row['direccion'].strip()
                    )
                    if centro:
                        centros_creados.append(centro)

    except FileNotFoundError:
        print(f"✗ Archivo no encontrado: {csv_path}")
    except Exception as e:
        print(f"✗ Error procesando CSV: {e}")

    print(f"\nResumen de carga:")
    print(f"  - Doctores creados: {len(doctores_creados)}")
    print(f"  - Pacientes creados: {len(pacientes_creados)}")
    print(f"  - Centros creados: {len(centros_creados)}")

    return doctores_creados, pacientes_creados, centros_creados


def main():
    """Función principal del script"""
    print("\n" + "="*60)
    print("  ODONTOCARE - Script de Carga Inicial")
    print("  Sistema de Gestión de Citas Dentales")
    print("="*60)

    # Crear cliente
    cliente = OdontoCareClient()

    # 1. Login con usuario admin
    if not cliente.login("admin", "admin123"):
        print("\n✗ No se pudo iniciar sesión. Asegúrese de que los servicios estén corriendo.")
        print("  Ejecute: docker-compose up -d")
        return

    # 2. Cargar datos desde CSV
    doctores, pacientes, centros = cargar_datos_csv(cliente, CSV_FILE)

    # 3. Crear una cita médica de ejemplo
    print(f"\n{'='*50}")
    print("Creando cita médica de ejemplo")
    print('='*50)

    # Obtener IDs de los elementos creados o existentes
    doctores_lista = cliente.listar_doctores()
    pacientes_lista = cliente.listar_pacientes()
    centros_lista = cliente.listar_centros()

    if doctores_lista and pacientes_lista and centros_lista:
        if (doctores_lista.get('doctores') and
            pacientes_lista.get('pacientes') and
            centros_lista.get('centros')):

            # Tomar el primer doctor, paciente y centro disponibles
            id_doctor = doctores_lista['doctores'][0]['id_doctor']
            id_paciente = pacientes_lista['pacientes'][0]['id_paciente']
            id_centro = centros_lista['centros'][0]['id_centro']

            # Fecha para mañana a las 10:00
            fecha_cita = (datetime.now() + timedelta(days=1)).replace(
                hour=10, minute=0, second=0, microsecond=0
            ).isoformat()

            cita = cliente.crear_cita(
                id_paciente=id_paciente,
                id_doctor=id_doctor,
                id_centro=id_centro,
                fecha=fecha_cita,
                motivo="Revisión dental general"
            )

            if cita:
                print(f"\n{'='*50}")
                print("JSON DE LA CITA CREADA:")
                print('='*50)
                print(json.dumps(cita, indent=2, ensure_ascii=False))
        else:
            print("✗ No hay suficientes datos para crear una cita")
    else:
        print("✗ No se pudieron obtener los datos necesarios")

    # 4. Mostrar resumen final
    print(f"\n{'='*50}")
    print("RESUMEN FINAL")
    print('='*50)

    citas_lista = cliente.listar_citas()
    if citas_lista:
        print(f"Total de citas en el sistema: {citas_lista.get('total', 0)}")

    print("\n✓ Carga inicial completada exitosamente")
    print("="*60)


if __name__ == "__main__":
    main()
