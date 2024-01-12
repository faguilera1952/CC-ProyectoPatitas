# :cat: Hito 4 :dog:

## Elección del sistema de Integración Continua (CI)

El objetivo de este hito 4 es preparar el proyecto para la integración continua. Debido a que se utiliza pytest para las pruebas unitarias y Docker para la contenerización el principal criterio de elección ha sido buscar un sistema de integración continua que sea compatible con estos frameworks y que ofrezca robustez y rapidez para la ejecución de los tests. Por consiguiente, para la elección del sistema integración continua se ha elegido Jenkins.

## Jenkins

Permite automatizar todo el proceso de construcción y ejecución de pruebas. Se puede configurar Jenkins para que automáticamente inicie la construcción del contenedor Docker y ejecute las pruebas unitarias cada vez que se realicen cambios en el código. Jenkins también permite hacer integración continua de manera robusta. Facilita la integración continua al proporcionar una ejecución automatizada de pruebas en cada cambio de código. Esto ayuda a identificar rápidamente problemas de integración y mantener una base de código estable.

## Configuración de Jenkins

Luego de descargado del sitio oficila, se ejecuta el la configuración de _Jenkins_ se elige por defecto el puerto 8080 que va a ejecutarse en el servidor local [localhost](http://localhost/8080). Se crea el usuario que en mi caso es _cisquito_ , luego se instalan todos los pluggins necesarios que se van a utilizar a efectos de este proyecto (GIT, Pipeline, Docker).

## Creación del Proyecto en Jenkins

Se procede luego a crear el nuevo proyecto en Jenkins, en mi caso se llama Patitas

![Patitas](/docs/img/2_jenkins.png).

## Configuracción de Github en Jenkins

Posteriormente se procede a conectar _Github_ dentro de _Jenkins_ mediante la URL dentro de la configuración general de _Jenkins

![Project url](/docs/img/4_jenkins.png)

## Configuración de la pipeline en Jenkins

También como parte de la configuración dentro de _Jenkins_ se configuran los _Build Triggers_: GitHub hook trigger for GITScm polling y Trigger builds remotely (e.g., from scripts) que permiten autenticar a las actions de Github.

Luego en la configuración de la pipeline se establece la direción del repositorio en github, la branch en donde se aloja este repositorio y el archivo Jenkinsfile que es el que contendrá los procesos a ejecutar cuando se ejecute algún cambio en el repositorio.

![pipeline](/docs/img/5_jenkins.png)

![pipelines](/docs/img/6_jenkins.png)

## Creación del archivo Jenkinsfile

Se crea el archivo [Jenkinsfile](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/Jenkinsfile) que proporciona una descripción del proceso de construcción y despliegue en Jenkins utilizando la sintaxis declarativa.

## Configuración del Webhook en Github

Dentro de la configuracion del repositorio, vamos a la popción de Webhook y creamos una nueva. En Payload URL colocamos la dirección de nuestro dashboard en _Jenkins_ que es a donde va a apuntar _Github_ cuando se ejecute algún cambio en el repositorio, en mi caso es webhook se va a  activar cuando se realice algún push dentro del repo.

Nota: Como GitHub no puede acceder a la URL del webhook de _Jenkins_ porque está configurada como "localhost", tuve que hacer uso de una aplicación llamada _ngrok_ para exponer mi servidor Jenkins local a una URL pública.

![webhook](/docs/img/7_github.png)

## Ejecución de las actions de GitHub y jobs de Jenkins

Mediante la configuración de _Webhook_ de _Github_ se estableció que cada vez que se haga una modificación al repositorio y se haga un push se ejecutarán las actions y además los jobs en _Jenkins_

![action](/docs/img/2_jenkins.png)

![action2](/docs/img/3_jenkins.png)
