# Tema 4. Microservicios y Contenedores

## 🗒️ Requisitos

Para realizar los ejercicios de este tema deberás tener configurado tu entorno de python.

### Librerías

Para los ejercicios que requieran librerías específicas, encontrarás archivos `requirements.txt` en las carpetas correspondientes.

> Nota: Cada sección puede tener sus propios requisitos. Por ejemplo, la sección 4e tiene su propio archivo requirements.txt.

## 📝 Enunciados

Los ejercicios los encontrarás organizados por carpetas según los apartados del tema. Cada ejercicio se presentará en un fichero python, que incluirá un comentario con el enunciado del ejercicio.

Los apartados del tema junto con los ejercicios son los siguientes:

| Apartado | Ejercicios |
| -------- | ---------- |
| a. Introducción a microservicios y contenedores | *No hay ejercicios en este apartado* |
| b. Primer ejemplo con Python y Docker | [ej4b1](4b/ej4b1.py) |
| c. Dockerfile construcción de imágenes | *No hay ejercicios en este apartado* |
| d. Gestión y publicación de imágenes | *No hay ejercicios en este apartado* |
| e. Ejemplo de aplicación con Flask y Docker | [ej4e1](4e/ej4e1.py) |

Además, cada ejercicio irá acompañado de uno o varios tests para comprobar que tu solución es correcta. 

Cuando hayas propuesto una implementación para la función, ejecuta los tests para ver si tu solución es correcta. Si no pasa los tests, vuelve a intentarlo revisando los errores que te comentan los tests.

Una vez termines el ejercicio, deberás enviar tus cambios para que se registren en la plataforma y que puedan ser corregidos por tu profesor. 

Si tienes alguna duda sobre cómo ejecutar los tests o cómo enviar los cambios a GitHub, consulta el ejercicio del Tema 0. Si todavía tienes algun comentario o problema, puedes escribir tu consulta en la plataforma de Preguntas y Respuestas de la Escuela de Programación.

## 💻 Comandos
En la siguiente sección se presentan algunos comandos útiles para el desarrollo de la actividad. 

### Git

Con el fin de actualizar los repositorios locales con la última versión de código fuente, ejecute:

```bash
git pull
```

Para agregar los cambios realizados en los archivos, ejecute:

```bash
git add .
```

Para añadir un mensaje a los cambios realizados localmente, ejecute:

```bash
git commit -m "Mensaje"
```

Para sincronizar nuestras modificaciones con el repositorio remoto, ejecute:
```bash
git push
```

### Python

Para ejecutar las pruebas unitarias:
```bash
pytest 
```
En caso de tener algún problema, puedes probar ejecutar la función con la instrucción `python -m` delante, por ejemplo:

```bash
python -m pytest 
```

### Docker

Para construir una imagen Docker:
```bash
docker build -t nombre-imagen .
```

Para ejecutar un contenedor Docker:
```bash
docker run -it --rm nombre-imagen
```

Para listar las imágenes Docker:
```bash
docker images
```

Para listar los contenedores Docker en ejecución:
```bash
docker ps
```

Más información sobre cómo ejecutar las pruebas unitarias, consulte el ejercicio del tema 0.
