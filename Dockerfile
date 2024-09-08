FROM python:latest

LABEL mantainer="hernansaa88@gmail.com"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

# Expone el servidor web de django en el puerto 8000
EXPOSE 8000

# Ejecutar los tests unitarios
RUN python3 manage.py test

# Comando para iniciar el servidor con el entorno virtual activado
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
