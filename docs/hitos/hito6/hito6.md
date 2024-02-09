# :cat: Hito 6 :dog:

## Composición de servicios

## Justificación de la estructura del clúster

La estructura del clúster presentada en el archivo de configuración [docker-compose.yml](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/docker-compose.yml) proporciona una organización clara y eficiente de los servicios y recursos necesarios para ejecutar y probar la aplicación. A continuación, se detalla la justificación de esta estructura:

- Servicios definidos: Cada servicio en el clúster está claramente definido en el archivo de configuración [docker-compose.yml](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/docker-compose.yml). Esto facilita la comprensión de los diferentes componentes de la aplicación y sus responsabilidades.

- Reutilización de imágenes y volúmenes: Todos los servicios (tests, app, api-test) comparten la misma configuración de construcción y volúmenes. Esto promueve la reutilización de imágenes Docker y volúmenes de datos, lo que reduce la duplicación y simplifica la administración del clúster.

- Gestión centralizada de volúmenes: Los volúmenes Docker están configurados para montar el directorio actual (.) en el contenedor en el directorio /app. Esto permite una gestión centralizada de los archivos de la aplicación y de las pruebas, lo que facilita el desarrollo y la ejecución de pruebas.

- Separación de responsabilidades: Los servicios tests y api-test están dedicados a la ejecución de pruebas automatizadas utilizando el marco de pruebas _pytest_. Esta separación de responsabilidades garantiza que las pruebas se ejecuten de forma aislada y controlada, lo que facilita la identificación y resolución de problemas.

- Exposición de puertos y redes: El servicio app expone el puerto _5000_ y se conecta a la red esta_mi_red. Esto permite que la aplicación sea accesible desde el exterior a través del puerto _5000_ y se comunique con otros servicios dentro de la misma red, si es necesario.

- Definición de redes personalizadas: Se define una red personalizada llamada esta_mi_red para conectar los servicios app y api-test. Esto proporciona un entorno de red aislado y controlado para la comunicación entre los servicios, lo que mejora la seguridad y la robustez del clúster.

## Fichero de composoción Del clúster

A continuación el archivo [docker-compose.yml](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/docker-compose.yml) orquesta y construye la aplicación _Patitas_. ste archivo de configuración de Docker Compose describe tres servicios (tests, app y api-test) que se ejecutarán como contenedores Docker. Cada servicio se define con su propia configuración de construcción, configuración de volumen, configuración de puerto y, en el caso de app, se conecta a una red llamada esta_mi_red. Entonces se detallará el significada de cada parámetro de la manera siguiente:

```text
        # Define la versión de la sintaxis de Docker Compose que se utilizará.
    version: '3'

        # Define los servicios que se ejecutarán como parte del clúster de Docker.
    services:

        # Servicio "tests":
    tests:
        # Construye la imagen del contenedor utilizando el Dockerfile del directorio actual.
        build: .
        # Monta el directorio actual en el directorio "/app" dentro del contenedor.
        volumes:
        - .:/app
        # Define el comando que se ejecutará cuando se inicie el contenedor, en este caso "pytest".
        command: ["pytest"]

        # Servicio "app":
    app:
        # Construye la imagen del contenedor utilizando el Dockerfile del directorio actual.
        build: .
        # Mapea el puerto 5000 del host al puerto 5000 del contenedor.
        ports:
        - "5000:5000"
        # Monta el directorio actual en el directorio "/app" dentro del contenedor.
        volumes:
        - .:/app
        # Conecta este servicio a la red llamada "esta_mi_red".
    networks:
        - esta_mi_red

        # Servicio "api-test":
    api-test:
        # Construye la imagen del contenedor utilizando el Dockerfile del directorio actual.
        build: .
        # Monta el directorio actual en el directorio "/app" dentro del contenedor.
        volumes:
        - .:/app
        # Define el comando que se ejecutará cuando se inicie el contenedor, en este caso "pytest test/test_profile.py".
        command: ["pytest", "test/test_profile.py"]

        # Servicio "docker-test":
    docker-test:
        # Indica que la imagen del contenedor se construye en el directorio actual
        build: .
        # Define los volúmenes que se montarán en el contenedor
        volumes:
        # Monta el directorio actual (donde se encuentra el archivo docker-compose.yml) en el directorio /app dentro del contenedor
        - .:/app
        # Define el comando que se ejecutará cuando el contenedor se inicie. En este caso, ejecutará pytest con el archivo test_docker.py como argumento.
        command: ["pytest", "test_docker.py"] 

        # Define una red llamada "esta_mi_red".
        networks:
    esta_mi_red:

```

## Fichero para realizar pruebas de salud y funcionamiento

Este fichero [test_docker.py](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/test/test_docker.py) se utiliza dentro de un contenedor para realizar pruebas automatizadas de salud y funcionamiento de la aplicación que se está ejecutando en el clúster de contenedores y para verificar que los contenedores del clúster se hayan levantado correctamente y que las rutas de la API Flask y de búsqueda estén respondiendo correctamente con un código de estado HTTP 200.

![cluster](/docs/img/cluster.png)
