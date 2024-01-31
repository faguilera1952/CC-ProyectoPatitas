from flasgger import Swagger
from flasgger.utils import swag_from
from flask import Flask, jsonify, request
import logging

from src.users.animal_profile import Animal

app = Flask(__name__)
swagger = Swagger(app)

# Configuración de logging para Flask
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

class Profile:
    def __init__(self):
        self.animals_for_adoption = []

    def add_animal(self, animal):
        self.animals_for_adoption.append(animal)
        app.logger.info(f"Nuevo animal agregado: {animal}")

    def search_animal(self, name):
        for animal in self.animals_for_adoption:
            if animal.name.lower() == name.lower():
                return animal
        return None

my_profile = Profile()

@app.route('/MariPulita', methods=['GET'])
def hello_world():
    """
    Endpoint para mostrar a la gatita MariPulita.
    ---
    responses:
      200:
        description: Respuesta exitosa
        schema:
          properties:
            Gata Azul Ruso:
              type: string
    """
    app.logger.info('Acceso a la ruta /MariPulita')
    return {'La gatita mas': 'linda'}

@app.route('/animals/add', methods=['POST'])
@swag_from('swagger/add_animal.yml')
def add_animal():
    """
    Agrega un nuevo animal.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Animal
          required:
            - name
            - age
            - species
            - description
          properties:
            name:
              type: string
              description: Nombre del animal.
            age:
              type: integer
              description: Edad del animal.
            species:
              type: string
              description: Especie del animal.
            description:
              type: string
              description: Descripción del animal.
    responses:
      201:
        description: Animal agregado exitosamente.
    """
    new_animal = request.json
    my_profile.add_animal(Animal(**new_animal))
    return jsonify({'message': 'Animal agregado exitosamente'}), 201

@app.route('/animals/search/<string:name>', methods=['GET'])
@swag_from('swagger/search_animal.yml')
def search_animal(name):
    app.logger.info(f"Búsqueda del animal: {name}")
    found_animal = my_profile.search_animal(name)
    if found_animal:
        animal_info = {
            'name': found_animal.name,
            'age': found_animal.age,
            'species': found_animal.species,
            'description': found_animal.description,
        }
        return jsonify(animal_info)
    else:
        app.logger.warning(f"Animal no encontrado: {name}")
        return jsonify({'message': 'Animal no encontrado'}), 404

if __name__ == '__main__':
    my_profile.add_animal(Animal("MariPulita", 2, "Gato", "Mi nina no se da nunca en adopción"))
    my_profile.add_animal(Animal("Vicenta", 1, "Gato", "Lo más lindo de casa"))
    app.run(debug=True)
