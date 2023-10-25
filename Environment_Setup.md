## Preparación del entorno de trabajo 🤖

Aquí se podrá seguir el paso a paso para preparar el repositorio de las prácticas.

### Repositorios

- [Fork del Repositorio original de Cloud Computing 23-24](https://github.com/cvillalonga/CC-23-24): Fork realizado desde el repositorio original de la asignatura de Cloud Computing.

- [Repositorio de mi Proyecto](https://github.com/faguilera1952/CC-ProyectoPatitas): Contiene el proyecto a desarrollar durante el transcurso de la asignatura.

### Configuración de la cuenta personal de GitHub:

Actualización de la imagen del perfil de mi cuenta en GiHub.

### Configuración de usuario y correo electrónico:

Se configura un nombre de usuario y una dirección de correo via comandos Git para asociarlo a la cuenta GitHub:

```
$ git config --global user.name "Francisco Aguilera Martínez"
$ git config --global user.email franciscoaguilera1990@gmail.com
```

Para listar los cambios realizados:

```
$ git config --list
```
![setup](/docs/img/userAndEmail.png)

### Generación de clave SSH y adición al agente SSH a GitHub:

Se generan las claves público/privada para conectar con el repositorio de GitHub mediante SSH.
Se usan los siguiente comandos:

```
$ ssh-keygen -t ed25519 -C "franciscoaguilera1990@gmail.com"
```
Luego el siguiente comando para añadir la clave SSH al agente SSH:

```
$ ssh-add ~/.ssh/id_xxxxxxx
```

![keys](/docs/img/sshKeys.png)
