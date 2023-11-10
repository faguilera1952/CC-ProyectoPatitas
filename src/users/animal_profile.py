class Profile:
    def __init__(self):
        self.animals_for_adoption = []

    def add_animal(self, animal):
        self.animals_for_adoption.append(animal)

    def search_animal(self, name):
        for animal in self.animals_for_adoption:
            if animal.name.lower() == name.lower():
                return animal
        return None

class Animal:
    def __init__(self, name, age, species, description):
        self.name = name
        self.age = age
        self.species = species
        self.description = description

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la clase Profile
    my_profile = Profile()

    # Agregar animales para adopción
    my_profile.add_animal(Animal("Buddy", 2, "Perro", "Cachorro juguetón en busca de un hogar"))
    my_profile.add_animal(Animal("Whiskers", 1, "Gato", "Gatito curioso y cariñoso"))

    # Buscar información de un animal por nombre
    animal_name_to_search = "Buddy"
    found_animal = my_profile.search_animal(animal_name_to_search)

    if found_animal:
        print(f"Información de {animal_name_to_search}:")
        print(f"Nombre: {found_animal.name}")
        print(f"Edad: {found_animal.age} años")
        print(f"Especie: {found_animal.species}")
        print(f"Descripción: {found_animal.description}")
    else:
        print(f"No se encontró información sobre {animal_name_to_search}")