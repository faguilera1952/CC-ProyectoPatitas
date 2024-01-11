# :cat: Hito 2 :dog:

## Elección del sistema de Integración Continua (CI)

El objetivo de este hito 4 es preparar el proyecto para la integración continua. Debido a que se utiliza pytest para las pruebas unitarias y Docker para la contenerización el principal criterio de elección ha sido buscar un sistema de integración continua que sea compatible con estos frameworks y que ofrezca robustez y rapidez para la ejecución de los tests. Por consiguiente, para la elección del sistema integración continua se ha elegido Jenkins.

## Jenkins

Permite automatizar todo el proceso de construcción y ejecución de pruebas. Se puede configurar Jenkins para que automáticamente inicie la construcción del contenedor Docker y ejecute las pruebas unitarias cada vez que se realicen cambios en el código. Jenkins también permite hacer integración continua de manera robusta. Facilita la integración continua al proporcionar una ejecución automatizada de pruebas en cada cambio de código. Esto ayuda a identificar rápidamente problemas de integración y mantener una base de código estable.
