# :cat: Hito 2 :dog:

## Gestor de tareas

Para llevar a cabo la realización de este proyecto, se usará "invoke" como gestor de tareas.  

## `invoke`

Es una herramienta en Python que se utiliza como un gestor de tareas o un sistema de automatización de tareas Proporcionar una manera simple y flexible de ejecutar comandos en la línea de comandos de manera programática, lo que es especialmente útil para la automatización de tareas en proyectos de desarrollo.

## Biblioteca de aserciones

Pytest proporciona la [biblioteca de aserciones](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/test/test_profile.py). Pytest utiliza el método "assert" para realizar las aserciones en las pruebas. En los bloques assert se están verificando varias condiciones y, si alguna de ellas falla, pytest informará sobre el error y detendrá la ejecución de las pruebas.

```
assert len(profile.animals_for_adoption) == 1
assert profile.animals_for_adoption[0] == animal
```

## `pytest`

[Pytest](tasks.py) es un marco de prueba unitaria para Python. Se utiliza específicamente para escribir y ejecutar pruebas unitarias y de integración en proyectos.

```
pytest
```

## TDD

El Desarrollo Guiado por Pruebas (TDD) es un enfoque de desarrollo de software en el que escribimos pruebas antes de escribir el código. En lugar de escribir código y luego probarlo, seguimos un ciclo que comienza con la creación de pruebas que describen el comportamiento deseado. Luego, escribimos el código necesario para que esas pruebas pasen. La principal razón para elegir el TDD es que ayuda a mejorar la calidad del código y reduce la probabilidad de introducir errores. 

## Contenido

A continuación, se describirán los pasos y tareas para llevar a cabo el hito 2.

## Creacion de un entorno virtual en windows

```text
python -m venv venv
```

## Activación del entorno virtual

```text
.\venv\Scripts\activate
```

## Instalación de invoke en el entorno virtual

```text
pip install invoke
```

## Ejecutar el test desde la terminal de VsCode

```text
.\venv\Scripts\invoke test
```
