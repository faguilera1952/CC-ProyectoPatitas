# :cat: Hito 2 :dog:

## Gestor de tareas

Para llevar a cabo la realización de este proyecto, se usará _"invoke_" como gestor de tareas. Es un marco (framework) para la automatización de tareas similares a _Make_ o _Fabric_, pero está diseñado específicamente para _Python_.

## `invoke`

Es una herramienta en Python que se utiliza como un gestor de tareas o un sistema de automatización de tareas Proporcionar una manera simple y flexible de ejecutar comandos en la línea de comandos de manera programática, lo que es especialmente útil para la automatización de tareas en proyectos de desarrollo.

## Biblioteca de aserciones

Pytest proporciona la [biblioteca de aserciones](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/test/test_profile.py). Pytest utiliza el método "assert" para realizar las aserciones en las pruebas. En los bloques assert se están verificando varias condiciones y, si alguna de ellas falla, pytest informará sobre el error y detendrá la ejecución de las pruebas.

```text
assert len(profile.animals_for_adoption) == 1
assert profile.animals_for_adoption[0] == animal
```

## `pytest`

[Pytest](/tasks.py) es un marco de prueba unitaria para Python. Se utiliza específicamente para escribir y ejecutar pruebas unitarias y de integración en proyectos.

```text
pytest
```

## TDD

El Desarrollo Guiado por Pruebas (TDD) es un enfoque de desarrollo de software en el que escribimos pruebas antes de escribir el código. En lugar de escribir código y luego probarlo, seguimos un ciclo que comienza con la creación de pruebas que describen el comportamiento deseado. Luego, escribimos el código necesario para que esas pruebas pasen. La principal razón para elegir el TDD es que ayuda a mejorar la calidad del código y reduce la probabilidad de introducir errores.

## Contenido

A continuación, se describirán los pasos y tareas para llevar a cabo el hito 2.

## Creacion de un entorno virtual en windows

Se crea un entorno virtual con _invoke_ en windows ya que es es una práctica recomendada para aislar las dependencias del proyecto y evitar futuros conflictos entre las mismas.

```text
python -m venv venv
```

## Activación del entorno virtual

Despues de creado es entorno virtual, se procede a la activación.

```text
.\venv\Scripts\activate
```

## Instalación de invoke en el entorno virtual

 Aqui nos aseguramos de que las dependencias y las herramientas específicas para este proyecto estén aisladas del sistema global de Python.

```text
pip install invoke
```

## Ejecución de los tests

Luego de haber creado y activado el entorno virtual, teniendo el test listo, se puede ejecutar el siguiente comando o bien desde la terminal de VSCode -en mi caso-, o desde una terminal que apunte a la raiz del proyecto.

En este caso, ya se ha definido una tarea _test_ en el archivo _tasks.py_ que utiliza _pytest_ para ejecutar las pruebas. Este comando invocará la tarea _test_ , y invoke ejecutará _pytest_ con el archivo de pruebas [test_profile.py](https://github.com/faguilera1952/CC-ProyectoPatitas/blob/main/test/test_profile.py):

```text
.\venv\Scripts\invoke test
```

También, si se prefiere se puede ejecutar las pruebas directamente con _pytest_ desde la línea de comandos:

```text
pytest test/test_profile.py
```

## Describiendo mi código inicial

1. Clase Animal en animal_profile.py:

Representa un animal con información básica para la adopción.

- Atributos: name, age, species, description.
- Métodos: __init__(self, name, age, species, description): Inicializa un nuevo objeto Animal con la información proporcionada.

2. Clase Profile en animal_profile.py:

Representa un perfil de adopción que contiene una lista de animales disponibles para adopción.

- Atributos: animals_for_adoption.
- Métodos: __init__(self), add_animal(self, animal), search_animal(self, name).

3. Ejemplo de uso en animal_profile.py:

Ejemplo de cómo usar las clases _Profile_ y _Animal_ para crear un perfil de adopción y realizar búsquedas.

- Acciones:
  - Crea una instancia de la clase Profile (my_profile).
  - Agrega dos animales (Buddy y Whiskers) a la lista de animales para adopción.
  - Realiza una búsqueda de información sobre un animal específico (Buddy) y muestra los detalles si se encuentra.

4. Pruebas unitarias en test_profile.py:

Verificar el correcto funcionamiento de las clases Profile y Animal.

- Pruebas:
  - test_add_animal(): Verifica que la función add_animal agrega correctamente un animal a la lista.
  - test_search_existing_animal(): Verifica que la función search_animal encuentra correctamente un animal existente.
  - test_search_nonexistent_animal(): Verifica que la función search_animal devuelve None para un animal inexistente.
  - test_search_case_insensitive(): Verifica que la búsqueda de animales sea insensible a mayúsculas y minúsculas.

5. Tarea test en tasks.py:

Ejecutar las pruebas utilizando pytest.

- Acciones: Utiliza la tarea test de Invoke para ejecutar las pruebas en el archivo test/test_profile.py.