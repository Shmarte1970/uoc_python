# OdontoCare API - Documentación de Endpoints

## Información General

- **Servicio de Usuarios**: `http://localhost:5001`
- **Servicio de Citas**: `http://localhost:5002`
- **Formato**: JSON
- **Autenticación**: Bearer Token (JWT)

---

## Servicio de Usuarios (Puerto 5001)

### Autenticación (auth_bp)

#### POST /auth/login
Iniciar sesión y obtener token JWT.

**Request:**
```json
{
    "username": "admin",
    "password": "admin123"
}
```

**Response (200):**
```json
{
    "mensaje": "Login exitoso",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "usuario": {
        "id_usuario": 1,
        "username": "admin",
        "rol": "admin"
    }
}
```

#### POST /auth/register
Registrar nuevo usuario (solo rol paciente).

**Request:**
```json
{
    "username": "nuevo_usuario",
    "password": "password123"
}
```

**Response (201):**
```json
{
    "mensaje": "Usuario registrado exitosamente",
    "usuario": {
        "id_usuario": 2,
        "username": "nuevo_usuario",
        "rol": "paciente"
    }
}
```

#### GET /auth/validate
Validar token JWT.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
    "valido": true,
    "usuario": {
        "id_usuario": 1,
        "username": "admin",
        "rol": "admin"
    }
}
```

---

### Administración (admin_bp)

#### POST /admin/usuario
Crear usuario (admin o secretaria). **Rol requerido: admin**

**Headers:** `Authorization: Bearer <token>`

**Request:**
```json
{
    "username": "secretaria1",
    "password": "secretaria123",
    "rol": "secretaria"
}
```

**Response (201):**
```json
{
    "mensaje": "Usuario creado exitosamente",
    "usuario": {
        "id_usuario": 3,
        "username": "secretaria1",
        "rol": "secretaria"
    }
}
```

#### GET /admin/usuarios
Listar todos los usuarios. **Rol requerido: admin**

**Response (200):**
```json
{
    "total": 3,
    "usuarios": [
        {"id_usuario": 1, "username": "admin", "rol": "admin"},
        {"id_usuario": 2, "username": "doctor1", "rol": "medico"}
    ]
}
```

---

### Doctores

#### POST /admin/doctores
Crear doctor. **Rol requerido: admin**

**Request:**
```json
{
    "nombre": "Dr. Juan García",
    "especialidad": "Odontología General",
    "username": "juan.garcia",
    "password": "doctor123"
}
```

**Response (201):**
```json
{
    "mensaje": "Doctor creado exitosamente",
    "doctor": {
        "id_doctor": 1,
        "id_usuario": 4,
        "nombre": "Dr. Juan García",
        "especialidad": "Odontología General"
    }
}
```

#### GET /admin/doctores
Listar todos los doctores. **Autenticación requerida**

#### GET /admin/doctores/{id}
Obtener doctor por ID. **Autenticación requerida**

#### PUT /admin/doctores/{id}
Actualizar doctor. **Rol requerido: admin**

#### DELETE /admin/doctores/{id}
Eliminar doctor. **Rol requerido: admin**

---

### Pacientes

#### POST /admin/pacientes
Crear paciente. **Rol requerido: admin, secretaria**

**Request:**
```json
{
    "nombre": "Pedro Sánchez",
    "telefono": "612345678",
    "estado": "ACTIVO",
    "username": "pedro.sanchez",
    "password": "paciente123"
}
```

**Response (201):**
```json
{
    "mensaje": "Paciente creado exitosamente",
    "paciente": {
        "id_paciente": 1,
        "id_usuario": 5,
        "nombre": "Pedro Sánchez",
        "telefono": "612345678",
        "estado": "ACTIVO"
    }
}
```

#### GET /admin/pacientes
Listar pacientes. **Autenticación requerida**

#### GET /admin/pacientes/{id}
Obtener paciente por ID. **Autenticación requerida**

#### PUT /admin/pacientes/{id}
Actualizar paciente. **Rol requerido: admin, secretaria**

#### DELETE /admin/pacientes/{id}
Eliminar paciente. **Rol requerido: admin**

---

### Centros Médicos

#### POST /admin/centros
Crear centro médico. **Rol requerido: admin**

**Request:**
```json
{
    "nombre": "Clínica Dental Centro",
    "direccion": "Calle Mayor 10, Madrid"
}
```

**Response (201):**
```json
{
    "mensaje": "Centro creado exitosamente",
    "centro": {
        "id_centro": 1,
        "nombre": "Clínica Dental Centro",
        "direccion": "Calle Mayor 10, Madrid"
    }
}
```

#### GET /admin/centros
Listar centros. **Autenticación requerida**

#### GET /admin/centros/{id}
Obtener centro por ID. **Autenticación requerida**

#### PUT /admin/centros/{id}
Actualizar centro. **Rol requerido: admin**

#### DELETE /admin/centros/{id}
Eliminar centro. **Rol requerido: admin**

---

## Servicio de Citas (Puerto 5002)

### Gestión de Citas (citas_bp)

#### POST /citas
Crear nueva cita. **Rol requerido: admin, secretaria, paciente**

**Request:**
```json
{
    "fecha": "2024-12-20T10:00:00",
    "motivo": "Revisión dental general",
    "id_paciente": 1,
    "id_doctor": 1,
    "id_centro": 1
}
```

**Response (201):**
```json
{
    "mensaje": "Cita creada exitosamente",
    "cita": {
        "id_cita": 1,
        "fecha": "2024-12-20T10:00:00",
        "motivo": "Revisión dental general",
        "estado": "PROGRAMADA",
        "id_paciente": 1,
        "id_doctor": 1,
        "id_centro": 1,
        "id_usuario_registra": 1,
        "created_at": "2024-12-19T15:30:00",
        "updated_at": "2024-12-19T15:30:00"
    }
}
```

**Validaciones:**
- El doctor debe existir
- El centro médico debe existir
- El paciente debe existir y estar ACTIVO
- No puede haber otra cita del mismo doctor en la misma fecha/hora

#### GET /citas
Listar citas según rol. **Autenticación requerida**

**Query params (según rol):**
- `fecha`: Filtrar por fecha (YYYY-MM-DD)
- `id_doctor`: Filtrar por doctor (solo admin)
- `id_centro`: Filtrar por centro (solo admin)
- `id_paciente`: Filtrar por paciente (solo admin)
- `estado`: Filtrar por estado (solo admin)

**Comportamiento por rol:**
- **medico**: Solo ve sus propias citas
- **secretaria**: Puede filtrar por fecha
- **admin**: Puede usar todos los filtros
- **paciente**: Solo ve sus propias citas

**Response (200):**
```json
{
    "total": 1,
    "citas": [
        {
            "id_cita": 1,
            "fecha": "2024-12-20T10:00:00",
            "motivo": "Revisión dental general",
            "estado": "PROGRAMADA",
            "id_paciente": 1,
            "id_doctor": 1,
            "id_centro": 1,
            "id_usuario_registra": 1
        }
    ]
}
```

#### GET /citas/{id}
Obtener cita por ID. **Autenticación requerida**

#### PUT /citas/{id}
Actualizar o cancelar cita. **Rol requerido: admin, secretaria**

**Request (cancelar):**
```json
{
    "estado": "CANCELADA"
}
```

**Request (actualizar):**
```json
{
    "motivo": "Cambio de motivo",
    "fecha": "2024-12-21T11:00:00"
}
```

**Response (200):**
```json
{
    "mensaje": "Cita cancelada exitosamente",
    "cita": {
        "id_cita": 1,
        "estado": "CANCELADA"
    }
}
```

**Validaciones:**
- La cita debe existir
- No se puede modificar una cita ya cancelada

#### DELETE /citas/{id}
Eliminar cita. **Rol requerido: admin**

#### GET /citas/doctor/{id}/disponibilidad
Verificar disponibilidad de un doctor. **Autenticación requerida**

**Query params:** `fecha` (YYYY-MM-DD)

**Response (200):**
```json
{
    "id_doctor": 1,
    "fecha": "2024-12-20",
    "horas_ocupadas": ["10:00", "11:00", "15:30"],
    "total_citas": 3
}
```

---

## Códigos de Error

| Código | Descripción |
|--------|-------------|
| 400 | Bad Request - Datos inválidos o incompletos |
| 401 | Unauthorized - Token no proporcionado o inválido |
| 403 | Forbidden - Sin permisos para este recurso |
| 404 | Not Found - Recurso no encontrado |
| 409 | Conflict - Conflicto (usuario/cita ya existe) |
| 500 | Internal Server Error |

---

## Roles y Permisos

| Rol | Descripción |
|-----|-------------|
| admin | Acceso completo a todos los endpoints |
| secretaria | Gestión de pacientes y citas |
| medico | Ver sus propias citas |
| paciente | Ver y crear sus propias citas |
