import pytest
import os
import sys

# Obtén la ruta del directorio actual (donde se encuentra test_profile.py)
current_dir = os.path.dirname(__file__)

# Agrega el directorio de nivel superior al sys.path
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))

from src.users.animal_profile import Profile, Animal

def test_add_animal():
    profile = Profile()
    animal = Animal("MariPulita", 2, "Gato", "Mi nina no se da nunca en adopcion")

    profile.add_animal(animal)

    assert len(profile.animals_for_adoption) == 1
    assert profile.animals_for_adoption[0] == animal

def test_search_existing_animal():
    profile = Profile()
    animal1 = Animal("MariPulita", 2, "Gato", "Mi nina no se da nunca en adopcion")
    animal2 = Animal("Vicenta", 1, "Gato", "Lo mas lindo de casa")

    profile.add_animal(animal1)
    profile.add_animal(animal2)

    found_animal = profile.search_animal("MariPulita")

    assert found_animal is not None
    assert found_animal.name == "MariPulita"

def test_search_nonexistent_animal():
    profile = Profile()
    animal = Animal("Vicenta", 1, "Gato", "Lo mas lindo de casa")

    profile.add_animal(animal)

    found_animal = profile.search_animal("Max")

    assert found_animal is None

def test_search_case_insensitive():
    profile = Profile()
    animal = Animal("MariPulita", 2, "Gato", "Mi nina no se da nunca en adopcion")

    profile.add_animal(animal)

    found_animal = profile.search_animal("MariPulita")

    assert found_animal is not None
    assert found_animal.name == "MariPulita"
