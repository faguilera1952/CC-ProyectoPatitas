import requests
import time

def test_cluster_health():
    # Espera a que los contenedores se levanten
    time.sleep(5)

    # Realiza una petición a la API Flask
    response = requests.get("http://localhost:5000/MariPulita")
    assert response.status_code == 200

    # Realiza una petición a la API de búsqueda
    response = requests.get("http://localhost:5000/animals/search/MariPulita")
    assert response.status_code == 200
