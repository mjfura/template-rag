# Imagen base de Miniconda
FROM continuumio/miniconda3

# Establece el directorio de trabajo
WORKDIR /app

# Crea el entorno Conda con Python 3.11.6 desde conda-forge
RUN conda create -n actividad_1 python=3.11.6 -y -c conda-forge

# Inicializa Conda en Bash
RUN conda init bash

# Copia el código fuente
COPY . .

# Asegura que Conda esté correctamente configurado al iniciar el contenedor
RUN echo "source /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
RUN echo "conda activate actividad_1" >> ~/.bashrc

# Cambia el shell predeterminado a Bash
SHELL ["/bin/bash", "-c"]

# Comando predeterminado para mantener el contenedor activo
CMD ["bash"]