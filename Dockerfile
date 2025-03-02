# Usa una imagen oficial de Python
FROM python:3.9

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios para la instalación de dependencias
COPY FigurasPorArticulo.py /app/
COPY KeyWordCloud.py /app/
COPY LinksFound.py /app/
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que correrá la app
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "-u", "FigurasPorArticulo.py"]
