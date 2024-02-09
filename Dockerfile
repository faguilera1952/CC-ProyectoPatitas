# Usa una imagen de Python como base
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el código del proyecto al contenedor
COPY . /app

# Instala las dependencias necesarias
RUN pip install -r requirements.txt  

# Comando por defecto para ejecutar las pruebas unitarias
#CMD ["pytest"]

# Comando por defecto para ejecutar Flask
#CMD ["python", "app.py"]

CMD ["sh", "-c", "pytest && python app.py"]