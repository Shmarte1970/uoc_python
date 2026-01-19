# OdontoCare - Sistema de Gestión de Citas Dentales

## Proyecto Final Python C1 - UOC

Sistema backend completo para una red de clínicas dentales, implementado con arquitectura de microservicios.

---

## Tecnologías Utilizadas

| Componente | Tecnología |
|------------|------------|
| Framework Backend | Flask + Blueprints |
| Base de Datos | SQLite + SQLAlchemy |
| Autenticación | JWT (PyJWT) |
| Contenedores | Docker + Docker Compose |
| Cliente | Python + Requests |

---

## Arquitectura del Sistema

El sistema está dividido en **2 microservicios independientes** que se comunican únicamente mediante REST:

```
┌─────────────────────┐     ┌─────────────────────┐
│  Servicio Usuarios  │     │   Servicio Citas    │
│     (Puerto 5001)   │◄────│    (Puerto 5002)    │
│                     │REST │                     │
│  - auth_bp          │     │  - citas_bp         │
│  - admin_bp         │     │                     │
│                     │     │                     │
│  [SQLite usuarios]  │     │  [SQLite citas]     │
└─────────────────────┘     └─────────────────────┘
```

### Servicio de Usuarios (Puerto 5001)
- Autenticación y gestión de tokens JWT
- CRUD de usuarios, doctores, pacientes y centros médicos

### Servicio de Citas (Puerto 5002)
- Gestión de citas médicas
- Comunicación con servicio de usuarios vía REST (no accede a su BD)
- Validaciones de negocio (disponibilidad, conflictos de horario)

---

## Estructura del Proyecto

```
odontocare/
├── servicio_usuarios/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── usuario.py
│   │   │   ├── paciente.py
│   │   │   ├── doctor.py
│   │   │   └── centro.py
│   │   └── blueprints/
│   │       ├── auth_bp.py
│   │       └── admin_bp.py
│   ├── config.py
│   ├── run.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── servicio_citas/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   └── cita.py
│   │   ├── blueprints/
│   │   │   └── citas_bp.py
│   │   └── services/
│   │       └── usuarios_client.py
│   ├── config.py
│   ├── run.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── docker-compose.yml

cliente/
├── carga_inicial.py      # Script de carga inicial
├── test_endpoints.py     # Pruebas de endpoints
└── requirements.txt

data/
└── datos.csv             # Datos iniciales

docs/
└── API_ENDPOINTS.md      # Documentación completa de la API
```

---

## Puesta en Marcha del Proyecto

### Requisitos Previos

- Docker Desktop instalado
- Python 3.11+ (para el cliente)

---

### PASO 1: Iniciar Docker Desktop

Antes de ejecutar cualquier comando, **Docker Desktop debe estar en ejecucion**.

1. Abrir Docker Desktop
2. Esperar a que el icono indique que esta activo (sin errores)
3. Verificar con: `docker --version`

---

### PASO 2: Levantar los Microservicios

```bash
# Abrir terminal en la carpeta del proyecto

# Ir a la carpeta de odontocare
cd odontocare

# Construir y ejecutar contenedores (primera vez)
docker-compose up --build

# Si ya esta construido, solo ejecutar
docker-compose up -d
```

**Verificar que los servicios estan activos:**
```bash
docker-compose ps
```

Debe mostrar:
- servicio_usuarios ... Up (puerto 5001)
- servicio_citas ... Up (puerto 5002)

---

### PASO 3: Ejecutar la Carga Inicial de Datos

```bash
# En otra terminal, ir a la carpeta cliente
cd cliente

# Instalar dependencias (solo la primera vez)
pip install -r requirements.txt

# Ejecutar carga inicial
python carga_inicial.py
```

Esto carga los datos del fichero `data/datos.csv` (doctores, pacientes, centros).

---

### PASO 4: Usar el Menu Interactivo

```bash
cd cliente
python menu_interactivo.py
```

**Credenciales:** admin / admin123

Este menu permite:
- Gestionar Doctores (listar, crear, buscar, eliminar)
- Gestionar Pacientes (listar, crear, modificar estado, eliminar)
- Gestionar Centros Medicos (listar, crear, eliminar)
- Gestionar Citas (listar, crear, cancelar, ver disponibilidad)

---

### Comandos Utiles de Docker

```bash
# Ver logs de los servicios
docker-compose logs -f

# Detener servicios
docker-compose down

# Reiniciar desde cero (elimina bases de datos)
docker-compose down -v
docker-compose up -d --build
```

---

## Endpoints Principales

### Servicio de Usuarios (Puerto 5001)

| Método | Endpoint | Descripción | Rol Requerido |
|--------|----------|-------------|---------------|
| POST | /auth/login | Login y obtener token | Público |
| POST | /auth/register | Registro de pacientes | Público |
| GET | /auth/validate | Validar token | Autenticado |
| POST | /admin/usuario | Crear usuario admin/secretaria | Admin |
| GET | /admin/usuarios | Listar usuarios | Admin |
| POST | /admin/doctores | Crear doctor | Admin |
| GET | /admin/doctores | Listar doctores | Autenticado |
| GET | /admin/doctores/{id} | Obtener doctor | Autenticado |
| PUT | /admin/doctores/{id} | Actualizar doctor | Admin |
| DELETE | /admin/doctores/{id} | Eliminar doctor | Admin |
| POST | /admin/pacientes | Crear paciente | Admin/Secretaria |
| GET | /admin/pacientes | Listar pacientes | Autenticado |
| GET | /admin/pacientes/{id} | Obtener paciente | Autenticado |
| PUT | /admin/pacientes/{id} | Actualizar paciente | Admin/Secretaria |
| DELETE | /admin/pacientes/{id} | Eliminar paciente | Admin |
| POST | /admin/centros | Crear centro | Admin |
| GET | /admin/centros | Listar centros | Autenticado |
| GET | /admin/centros/{id} | Obtener centro | Autenticado |
| PUT | /admin/centros/{id} | Actualizar centro | Admin |
| DELETE | /admin/centros/{id} | Eliminar centro | Admin |

### Servicio de Citas (Puerto 5002)

| Método | Endpoint | Descripción | Rol Requerido |
|--------|----------|-------------|---------------|
| POST | /citas | Crear cita | Admin/Secretaria/Paciente |
| GET | /citas | Listar citas (filtros según rol) | Autenticado |
| GET | /citas/{id} | Obtener cita | Autenticado |
| PUT | /citas/{id} | Actualizar/Cancelar cita | Admin/Secretaria |
| DELETE | /citas/{id} | Eliminar cita | Admin |
| GET | /citas/doctor/{id}/disponibilidad | Ver disponibilidad | Autenticado |

Ver documentación completa en [docs/API_ENDPOINTS.md](docs/API_ENDPOINTS.md)

---

## Modelo de Datos

### Usuario
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_usuario | Integer (PK) | Identificador único |
| username | String | Nombre de usuario |
| password | String | Contraseña (hash) |
| rol | String | admin, medico, secretaria, paciente |

### Paciente
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_paciente | Integer (PK) | Identificador único |
| id_usuario | Integer (FK) | Referencia a usuario |
| nombre | String | Nombre completo |
| telefono | String | Teléfono de contacto |
| estado | String | ACTIVO / INACTIVO |

### Doctor
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_doctor | Integer (PK) | Identificador único |
| id_usuario | Integer (FK) | Referencia a usuario |
| nombre | String | Nombre completo |
| especialidad | String | Especialidad médica |

### Centro Médico
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_centro | Integer (PK) | Identificador único |
| nombre | String | Nombre del centro |
| direccion | String | Dirección física |

### Cita Médica
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_cita | Integer (PK) | Identificador único |
| fecha | DateTime | Fecha y hora de la cita |
| motivo | String | Motivo de la consulta |
| estado | String | PROGRAMADA / COMPLETADA / CANCELADA |
| id_paciente | Integer (FK) | Referencia a paciente |
| id_doctor | Integer (FK) | Referencia a doctor |
| id_centro | Integer (FK) | Referencia a centro |
| id_usuario_registra | Integer (FK) | Usuario que registró |

---

## Ejemplos de Uso con cURL

### 1. Login
```bash
curl -X POST http://localhost:5001/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

### 2. Crear Doctor (con token)
```bash
curl -X POST http://localhost:5001/admin/doctores \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"nombre": "Dr. García", "especialidad": "Ortodoncia", "username": "dr.garcia", "password": "doc123"}'
```

### 3. Crear Paciente
```bash
curl -X POST http://localhost:5001/admin/pacientes \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"nombre": "Juan Pérez", "telefono": "600123456", "estado": "ACTIVO"}'
```

### 4. Crear Centro
```bash
curl -X POST http://localhost:5001/admin/centros \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"nombre": "Clínica Centro", "direccion": "Calle Mayor 10"}'
```

### 5. Crear Cita
```bash
curl -X POST http://localhost:5002/citas \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"id_paciente": 1, "id_doctor": 1, "id_centro": 1, "fecha": "2024-12-20T10:00:00", "motivo": "Revisión dental"}'
```

### 6. Listar Citas
```bash
curl -X GET http://localhost:5002/citas \
  -H "Authorization: Bearer <TOKEN>"
```

### 7. Cancelar Cita
```bash
curl -X PUT http://localhost:5002/citas/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"estado": "CANCELADA"}'
```

---

## Credenciales por Defecto

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| admin | admin123 | admin |

---

## Reglas de Negocio

1. **Autenticación**: Todos los endpoints (excepto login y register) requieren token JWT
2. **Doble reserva**: No se puede agendar una cita si el doctor ya tiene otra en la misma fecha/hora
3. **Paciente activo**: Solo se pueden crear citas para pacientes con estado ACTIVO
4. **Cancelación**: Las citas canceladas no pueden ser modificadas
5. **Roles**:
   - **Admin**: Acceso completo
   - **Secretaria**: Gestión de pacientes y citas
   - **Médico**: Ver sus propias citas
   - **Paciente**: Ver y crear sus propias citas

---

## Comunicación entre Microservicios

El servicio de citas **NO accede directamente** a la base de datos de usuarios. En su lugar:

1. Valida tokens llamando a `/auth/validate`
2. Obtiene información de doctores, pacientes y centros vía REST
3. Almacena solo los IDs de referencia en su propia base de datos

---

## Autor

Proyecto Final - Python C1
Escuela de Programación - Universitat Oberta de Catalunya (UOC)

---

## Licencia

Este proyecto es parte del material educativo de la UOC.
