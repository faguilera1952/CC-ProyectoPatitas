# :cat: Hito 5 :dog:

## Framework para el Microservicio

Tal y como se estableció en el [hito 1](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/docs/hitos/hito1/hito1.md), para la realización del proyecto se ha hecho uso del framework de _Flask_ y adicionalmente también se estudió la posibilidad de agregar _Swagger_, entonces, a continuación se dará la justificación.

## Justificación de elección de Flask y Swagger

Elegí utilizar Flask en combinación con Swagger para desarrollar y documentar mis APIs por varias razones fundamentales. En primer lugar, Flask proporciona un marco ágil y fácil de usar para construir aplicaciones web, permitiéndome desarrollar rápidamente APIs eficientes y escalables. La elección de Swagger se basa en su capacidad para generar documentación interactiva y visualmente atractiva directamente desde el código, lo que facilita la comprensión y prueba de las API sin la necesidad de herramientas externas. Esta integración mejora la colaboración entre los desarrolladores y los equipos al proporcionar una interfaz clara y dinámica para explorar y probar las funcionalidades de las APIs, lo que resulta en un desarrollo más eficiente y una documentación más completa.

## Implementación de _logging libraries_ para el registro de logs

Una de las bibliotecas más comunes y poderosas para el registro en Python es la biblioteca estándar _logging_. La implementación de logging libraries en el código Python junto con las APIs desarrolladas en _Flask_ y _Swagger_ tiene un impacto significativo en la calidad y mantenimiento del software. La integración de registros permite una trazabilidad efectiva de la ejecución de las APIs, proporcionando información crucial sobre el flujo de datos, operaciones realizadas y posibles problemas. Estos registros facilitan la identificación y solución de errores, así como el seguimiento de eventos importantes durante la ejecución de la aplicación. Además, la configuración de registros contribuye a la transparencia, ya que proporciona una visión detallada de la actividad de la aplicación. Esta práctica se traduce en un desarrollo más eficiente, una depuración simplificada y una mayor capacidad para mantener y mejorar las APIs a lo largo del tiempo.

## Configuración de Flask y Swagger

Primero ingresamos al entorno virtual del proyecto con el comando:

        ```text
        .\venv\Scripts\activate
        ```
Estando dentro del entorno virtual del proyecto instalamos las librerias de Flask y Swagger:

        ```
        Flask 3.0.1
        ```

y luego _flasgger

        ```
        flasgger 0.9.7.1
        ```

por ultimo también necesitamos Werkzeug para manejar la parte de servidor web y proporcionar la infraestructura necesaria para gestionar las solicitudes y respuestas HTTP:

        ```
        Werkzeug 3.0.1
        ```

![entorno virtual](/docs/img/piplist.png)

## Creación del fichero app.py que contiene los métodos de la API

[app.py](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/app.py) es un archivo Python que define una aplicación web utilizando el framework Flask. En este archivo, se crea una aplicación Flask llamada _app_ que incluye rutas para gestionar endpoints relacionados con la adopción y búsqueda de animales. Además, se utiliza la extensión Flask-Swagger para generar documentación automática de la API, y se implementa un sistema de logging para registrar información relevante. La aplicación contiene tres rutas principales: /MariPulita, un endpoint para mostrar información sobre una gatita, /animals/add, un endpoint para agregar nuevos animales a una lista de adopción, y /animals/search/<string:name>, un endpoint para buscar información sobre un animal específico. El código también instancia un objeto Profile para gestionar la lista de animales para adopción y registra eventos importantes utilizando el sistema de logging de Flask. Finalmente, en el bloque if __name__ == '__main__':, se añaden dos animales de ejemplo a la lista y la aplicación se ejecuta en modo debug.

## Creación de ficheros de especificación OpenAPI

Se crean dentro de la carpeta [Swagger](https://github.com/faguilera1952/CC-ProyectoPatitas/tree/main/swagger) los ficheros [add_animal.yml](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/swagger/add_animal.yml) y [search_animal.yml](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/swagger/search_animal.yml) en donde se definen los detalles de cómo interactuar con la API, qué datos deben proporcionarse en la solicitud y qué se puede esperar como respuesta.

## Inicialización de la aplicación Flask

Estando dentro del entorno virtual del proyecto se procede a ejecutar el comando:

        ```
        python app.py
        ```
Este archivo _app.py_ define una aplicación web utilizando el framework Flask. Cuando se ejecuta python app.py, se inicializa la aplicación Flask llamada app. Esto implica que se configuran las rutas, se establecen las configuraciones de la aplicación, y se prepara la aplicación para manejar solicitudes web:

![python app.py](/docs/img/app.png)

Luego de haber ejecutado ese comando de inicialización vamos a la ruta web local de [Swagger](http://127.0.0.1:5000/apidocs/) para ver como se muestran las API´s creadas:

![apis](/docs/img/swagger1.png)

Dentro de _apidocs_ podemos ver los métodos GET y POST creados.

## Registros de logs de las API´s

Se agrega la configuración de _logging_ a la aplicación Flask para que los registros se almacenen en un [archivo](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/app.log) que es generado y se guardo en el local del proyecto. Se importa la libreria _import logging_ en el archivo app.py

        ```
        # Configuración de logging para Flask
        logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)
        ```
![logs](/docs/img/logs.png)
