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

## Creacion del archivo Dokerfile

Se crea manualmente el archivo Dokerfile, que es un archivo de configuración utilizado en Docker para construir imágenes de contenedores. El propósito principal del archivo Dockerfile es proporcionar una receta o conjunto de instrucciones paso a paso para construir una imagen de contenedor. Al construir la imagen, Docker seguirá estas instrucciones para crear un entorno reproducible y consistente.

- FROM: Indica la imagen base que se utilizará como punto de partida. Establece el directorio de trabajo en el contenedor.
- WORKDIR /app: Establece el directorio de trabajo en el contenedor.
- COPY . /app: Copia el código del proyecto al contenedor.
- CMD ["pytest"]: Comando por defecto para ejecutar las pruebas unitarias.

## Creación del archivo docker-compose.yml

Se crea manualmente el archivo para simplificar la ejecución del contenedor.

## Ejecución del contenedor

Se abre una terminal en el directorio del proyecto y se ejecuta el siguiente comando para construir la imagen del contenedor:

```text
docker-compose build
```

Obteniendo el siguiente resultado:

![doker build](/docs/img/doker 1.png)

Luego para iniciar los servicios definidos en el archivo docker-compose.yml se ejecuta el siguiente comando:

```text
docker-compose up
```

Obteniendo el siguiente resultado:

![doker up](/docs/img/doker 2.png)

## Después de que la imagen se haya construido, se ejecuta las pruebas unitarias

Esta acción montará el directorio actual dentro del contenedor y ejecutará el comando por defecto (pytest en este caso)

```text
docker-compose run tests
```

Obteniendo el siguiente resultado:

![doker tests](/docs/img/doker 3.png)
