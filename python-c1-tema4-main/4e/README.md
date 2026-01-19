# Enunciado de la Práctica: Creación de un Contenedor Docker para una Aplicación Flask

## Objetivo:

El objetivo de esta práctica es que los estudiantes aprendan a crear un `Dockerfile` para una aplicación web simple desarrollada en Flask, y luego construir una imagen Docker y ejecutar un contenedor a partir de ella.

## Tareas a Realizar:

1.  **Completar el `Dockerfile`:**
    *   Deberán completar los comentarios y las líneas de código faltantes en el `Dockerfile` proporcionado.
    *   Asegúrense de que el `Dockerfile` realice las siguientes acciones:
        *   Utilice una imagen base de Python.
        *   Establezca un directorio de trabajo dentro del contenedor.
        *   Copie el archivo `requirements.txt` e instale las dependencias.
        *   Copie el resto de los archivos de la aplicación.
        *   Exponga el puerto correcto donde la aplicación Flask escuchará.
        *   **Cree un usuario no root llamado "usertest" y configure los permisos adecuados.**
        *   Defina el comando para ejecutar la aplicación Flask.

2.  **Construir la Imagen Docker:**
    *   Una vez que el `Dockerfile` esté completo, deberán construir la imagen Docker utilizando el comando `docker build`.
    *   Asignen un nombre significativo a su imagen (por ejemplo, `mi-app-flask-practica`).

3.  **Ejecutar el Contenedor Docker:**
    *   Finalmente, deberán ejecutar un contenedor a partir de la imagen que crearon.
    *   Asegúrense de mapear el puerto del contenedor al puerto de su máquina local para poder acceder a la aplicación desde el navegador.

## Verificación:

*   Después de ejecutar el contenedor, abran su navegador y visiten `http://localhost:5000` (o el puerto que hayan elegido).
*   Deberían ver una respuesta JSON similar a la siguiente:
    ```json
    {
        "mensaje": "¡Hola, este es el primer ejemplo con Docker!",
        "usuario": "usertest",
        "pid": 1,
        "uid": 1000
    }
    ```
*   **Importante:** La aplicación debe estar ejecutándose como el usuario `usertest` dentro del contenedor, no como `root`, lo que se verifica en la respuesta JSON.

¡Mucha suerte con el ejercicio!
