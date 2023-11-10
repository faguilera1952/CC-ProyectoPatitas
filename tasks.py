# tasks.py

from invoke import task

@task
def test(c):
    """
    Ejecutar pruebas con pytest
    """
    c.run("pytest test/test_profile.py")
