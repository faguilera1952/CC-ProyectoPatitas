# Elección del contenedor base

La elección del contenedor base a utilizar se basa en función a las decisiones tomadas en el [Hito 2](./../hito2/hito2.md) y teniendo en cuentas las herramientas, los frameworks y lenguajes que se emplearán. Al crear un contenedor Docker para una aplicación en _Python_, generalmente se comienza seleccionando una imagen base de _Python_ oficial. Estas imágenes son proporcionadas por la comunidad de Docker y están optimizadas para ejecutar aplicaciones Python. Algunas de las imágenes base populares para Python incluyen:

- python: Esta es la imagen oficial de Python y está disponible con diferentes versiones y la elejida como contenedor base con la versión 3.9.

```text
FROM python:3.9
```

- alpine: También hay imágenes más ligeras basadas en Alpine Linux que son conocidas por ser más pequeñas en tamaño.

```text
FROM python:3.9-alpine
```

- slim: Las imágenes "slim" son versiones más ligeras de las imágenes oficiales y son una opción intermedia entre las versiones completas y las versiones alpinas.

```text
FROM python:3.9-slim
```

## Configuración del contenedor

- Primero creamos el archivo _requirements.txt_ usando el comando desde el directorio raiz del proyecto:

```text
pip freeze > requirements.txt
```

Este comando captura todas las dependencias instaladas en el entorno actual de Python y las escribe en un archivo llamado requirements.txt. Esto asegura que las mismas dependencias estén disponibles en el contenedor Docker.

## Creacion del archivo Dockerfile

Se crea manualmente el archivo Dokerfile, que es un archivo de configuración utilizado en Docker para construir imágenes de contenedores. El propósito principal del archivo Dockerfile es proporcionar una receta o conjunto de instrucciones paso a paso para construir una imagen de contenedor. Al construir la imagen, Docker seguirá estas instrucciones para crear un entorno reproducible y consistente.

- `FROM`: Indica la imagen base que se utilizará como punto de partida. Establece el directorio de trabajo en el contenedor.
- `WORKDIR /app`: Establece el directorio de trabajo en el contenedor.
- `COPY . /app`: Copia el código del proyecto al contenedor.
- `CMD ["pytest"]`: Comando por defecto para ejecutar las pruebas unitarias.

## Creación del archivo docker-compose.yml

Se crea manualmente el archivo para simplificar la ejecución del contenedor.

## Ejecución del contenedor

Se abre una terminal en el directorio del proyecto y se ejecuta el siguiente comando para construir la imagen del contenedor:

```text
docker-compose build
```

Obteniendo el siguiente resultado:

![docker build](/docs/img/docker_1.png)

Luego para iniciar los servicios definidos en el archivo docker-compose.yml se ejecuta el siguiente comando:

```text
docker-compose up
```

Obteniendo el siguiente resultado:

![docker up](/docs/img/docker_2.png)

## Después de que la imagen se haya construido, se ejecuta las pruebas unitarias

Esta acción montará el directorio actual dentro del contenedor y ejecutará el comando por defecto (pytest en este caso)

```text
docker-compose run tests
```

Obteniendo el siguiente resultado:

![docker tests](/docs/img/docker_3.png)

## Después se procede a etiquetar la imagen local con el nombre del usuario de Docker Hub y el nombre de la imagen que se desea en Docker Hub

```text
docker tag cisquito/cc-proyectopatitas-tests:latest cisquito/cc-proyectopatitas-tests:latest
```

![docker tag](/docs/img/docker_4.png)

## Por último se procede a hacer el push de la imagen etiquetada local al Docker Hub

```text
docker push cisquito/cc-proyectopatitas-tests:latest
```

![docker push](/docs/img/docker_5.png)

## Acciones programadas mediante GitHub Actions

GitHub Actions utiliza webhooks para activar flujos de trabajo [aquí](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/github/workflows/update-imagen.yml) automáticamente cuando se producen ciertos eventos en el repositorio de GitHub. En este caso los webhooks activan flujos de trabajo basados en eventos como un push.

1. Crear un Archivo de Flujo de Trabajo.

    ```text
    Archivo YML en la ruta .github/workflows/update-imagen.yml Este archivo contendrá la configuración para el flujo de trabajo.
    ```

2. Configurar el Flujo de Trabajo.

    ```text
    jobs:
    build:
        runs-on: windows-latest

        steps:
        - name: Checkout Repo
            uses: actions/checkout@v2

        - name: Build Docker Image
            run: docker build -t tu-usuario/nombre-imagen:etiqueta .

        - name: Login a Docker Hub
            run: echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin

        - name: Push a Docker Hub
            run: docker push cisquito/cc-proyectopatitas-tests:latest

    ```

3. Configurar Secretos en GitHub.

    ```text
    En la configuración del repositorio en GitHub, en la sección "Settings" y luego "Secrets" se agregan _DOCKER_USERNAME_ y _DOCKER_PASSWORD_ con las credenciales de Docker Hub.
    ```

4. Ejecutar el Flujo de Trabajo.

    ```text
    Hacer un push desde el directorio del proyecto.
    ```
