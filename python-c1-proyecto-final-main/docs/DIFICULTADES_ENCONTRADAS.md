# Dificultades Encontradas y Soluciones

## Proyecto OdontoCare - Python C1

Este documento describe los problemas encontrados durante el desarrollo y las soluciones aplicadas.

---

## Problema 1: Error en el formato del archivo CSV

### Descripcion del problema

Al ejecutar el script `carga_inicial.py`, los pacientes se creaban con el estado incorrecto. En lugar de tener estado "ACTIVO", se guardaba "paciente123" (que era la contrasena).

### Causa raiz

El archivo `datos.csv` tenia un error en la estructura de columnas. Habia una columna extra vacia que desplazaba los valores:

**CSV incorrecto:**
```csv
tipo,nombre,especialidad,telefono,direccion,username,password,estado
paciente,Pedro Sanchez,,612345678,,,pedro.sanchez,paciente123,ACTIVO
```

El problema era que habia una coma extra antes de `pedro.sanchez`, lo que creaba una columna vacia adicional. Esto causaba que:
- La columna `username` recibiera un valor vacio
- La columna `password` recibiera "pedro.sanchez"
- La columna `estado` recibiera "paciente123"

### Solucion aplicada

Se corrigio el archivo CSV eliminando las comas extras y alineando correctamente las columnas:

**CSV corregido:**
```csv
tipo,nombre,especialidad,telefono,direccion,username,password,estado
paciente,Pedro Sanchez,,612345678,,pedro.sanchez,paciente123,ACTIVO
```

La diferencia esta en que ahora hay exactamente una coma entre cada campo, sin espacios extra ni comas duplicadas.

---

## Problema 2: Pacientes existentes con estado incorrecto

### Descripcion del problema

Despues de corregir el CSV, los pacientes que ya existian en la base de datos seguian teniendo el estado incorrecto ("paciente123" en lugar de "ACTIVO").

### Causa raiz

La base de datos SQLite de Docker ya tenia los registros creados con el valor erroneo. Corregir el CSV solo afecta a nuevos registros.

### Solucion aplicada

Se actualizo el paciente existente mediante una peticion PUT al endpoint de actualizacion:

```bash
curl -X PUT http://localhost:5001/admin/pacientes/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"estado": "ACTIVO"}'
```

Esto cambio el estado del paciente de "paciente123" a "ACTIVO", permitiendo crear citas correctamente.

### Solucion alternativa

Otra opcion es reiniciar los contenedores eliminando los volumenes para empezar con una base de datos limpia:

```bash
docker-compose down -v
docker-compose up -d
```

El flag `-v` elimina los volumenes asociados, lo que borra las bases de datos y permite empezar desde cero.

---

## Problema 3: Error "El paciente no esta activo" al crear citas

### Descripcion del problema

Al intentar crear una cita, el sistema rechazaba la peticion con el mensaje "El paciente no esta activo".

### Causa raiz

Este error era consecuencia del Problema 1. El servicio de citas validaba que el paciente tuviera estado "ACTIVO", pero el paciente tenia estado "paciente123" debido al error del CSV.

### Solucion aplicada

Se resolvio al corregir el CSV (Problema 1) y actualizar los pacientes existentes (Problema 2).

### Validacion en el codigo

El codigo que realiza esta validacion se encuentra en `servicio_citas/app/blueprints/citas_bp.py`:

```python
# Validar que el paciente existe y esta activo
paciente = UsuariosServiceClient.obtener_paciente(id_paciente, token)
if not paciente:
    return jsonify({'error': f'Paciente con ID {id_paciente} no encontrado'}), 404

if paciente.get('estado') != 'ACTIVO':
    return jsonify({'error': 'El paciente no esta activo'}), 400
```

---

## Problema 4: Docker Desktop no iniciado

### Descripcion del problema

Al ejecutar `docker-compose up --build`, aparecia el error:
```
unable to get image 'odontocare-servicio_usuarios': error during connect:
open //./pipe/dockerDesktopLinuxEngine: El sistema no puede encontrar el archivo especificado.
```

### Causa raiz

Docker Desktop no estaba ejecutandose en el sistema.

### Solucion aplicada

Se inicio Docker Desktop desde el menu de Windows y se espero a que el icono en la bandeja del sistema indicara que estaba "Running".

---

## Problema 5: Warning de version obsoleta en docker-compose

### Descripcion del problema

Al ejecutar docker-compose aparecia el warning:
```
level=warning msg="docker-compose.yml: the attribute `version` is obsolete"
```

### Causa raiz

Las versiones recientes de Docker Compose ya no requieren el atributo `version` en el archivo YAML.

### Solucion aplicada

Este warning es informativo y no afecta el funcionamiento. Se puede ignorar o eliminar la linea `version: '3.8'` del archivo `docker-compose.yml`.

---

## Lecciones aprendidas

1. **Validar datos de entrada:** Siempre verificar que los archivos CSV tengan el formato correcto antes de procesarlos.

2. **Logs de depuracion:** Agregar logs para ver que datos se estan enviando ayuda a identificar problemas rapidamente.

3. **Pruebas incrementales:** Es mejor probar cada componente por separado antes de integrar todo.

4. **Documentar errores:** Mantener un registro de los errores encontrados y sus soluciones facilita la resolucion de problemas futuros.

---

## Comandos utiles para depuracion

### Ver los pacientes en el sistema:
```bash
curl http://localhost:5001/admin/pacientes -H "Authorization: Bearer <TOKEN>"
```

### Reiniciar todo desde cero:
```bash
docker-compose down -v
docker-compose up -d --build
```

### Ver logs de los contenedores:
```bash
docker-compose logs -f
```

### Verificar que los servicios responden:
```bash
curl http://localhost:5001/health
curl http://localhost:5002/health
```
