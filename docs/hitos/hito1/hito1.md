# :computer: Hito 1 :computer:

> Versión 1.0.1

## Contenidos

- [Historias de usuario](#hus)
- [Milestones](#milestones)
- [Estructura inicial](#initialStructure)
- [Lenguajes y _frameworks_](#framework)

<a name="hus"></a>

## Historias de usuario

A continuación, se definirán las siguientes historias de usuario:

- [HU1 - Como usuario quiero poder buscar la información de un animalito en adopción.](https://github.com/faguilera1952/CC-ProyectoPatitas/issues/1)
- [HU2 - Como usuario quiero obtener información sobre todos los animales en adopción.](https://github.com/faguilera1952/CC-ProyectoPatitas/issues/2)
- [HU3 - Como administrador quiero almacenar la información de un animalito en adopción.](https://github.com/faguilera1952/CC-ProyectoPatitas/issues/3)
- [HU4 - Como usuario quiero poder crear una cuenta y registrarme en la aplicación.](https://github.com/faguilera1952/CC-ProyectoPatitas/issues/4)
- [HU5 - Como administrador quiero poder modificar, actualizar, eliminar los datos de un animalito en adopción.](https://github.com/faguilera1952/CC-ProyectoPatitas/issues/5)

<a name="milestones"></a>

## Milestones

Se realizará la planificación del proyecto en diferentes _milestones_ definidos a continuación:

- [Hito 1: Creación y definición del proyecto.](https://github.com/faguilera1952/CC-ProyectoPatitas/milestone/1)
- [Hito 2: Desarrollo Inicial y pruebas unitarias.](https://github.com/faguilera1952/CC-ProyectoPatitas/milestone/2)
- [Hito 3: Contenedores para las pruebas de Integración.](https://github.com/faguilera1952/CC-ProyectoPatitas/milestone/3)
- [Hito 4: Integración continua.](https://github.com/faguilera1952/CC-ProyectoPatitas/milestone/4)
- [Hito 5: Creación del servicio.](https://github.com/faguilera1952/CC-ProyectoPatitas/milestone/5)
- [Hito 6: Preparación de un servicio con contenedores.](https://github.com/faguilera1952/CC-ProyectoPatitas/milestone/6)
-[Hito 7: Despliegue](https://github.com/faguilera1952/CC-ProyectoPatitas/milestone/7)

<a name="initialStructure"></a>

## Estructura inicial del proyecto

La estructura inicial del proyecto contendrá las siguientes clases o entidades:

- **Profile**: xxx [fichero](./../../backend/src/modules/users/nnn).
- **User**: xxx [fichero](./../../backend/src/modules/users/nnn).
- **Book**: xxx [fichero](./../../backend/src/modules/books/nnnn).

<!-- Books: Guarda toda la información obtenida del archivo JSON además de funcionalidades básicas. Se encuentra definida en el [fichero](/libs/entity-data-models/src/entities/crud.entity.ts).-->

<a name="framework"></a>

## Lenguajes y _frameworks_

Para la realización del proyecto se utilizarán los siguietes lenguajes y frameworks:

- Frontend (Lado del Cliente):

Angular: Un framework de desarrollo de aplicaciones web que permitirá crear la interfaz de usuario (UI). Angular es un framework de código abierto desarrollado por Google.

- Backend (Lado del Servidor):

Python: Se usará Python como lenguaje de programación en el lado del servidor para desarrollar las funcionalidades del servidor la aplicación.

Flask: Flask es un framework web ligero de Python que ayudará a crear el servidor y las rutas para la aplicación. Es conocido por su simplicidad y facilidad de uso.

- Contenerización:

Docker: Se utilizarás Docker para contenerizar servicios, como el servidor Flask y la aplicación Angular, lo que facilitará el despliegue y la gestión de los componentes de la aplicación.

Github: Un sistema de control de versiones que ayudará a rastrear y gestionar cambios en el código fuente del proyecto.

Docker Compose: Una herramienta que permitirá orquestar y administrar contenedores y simplificar la ejecución de servicios relacionados.