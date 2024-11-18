# Imagen base de Miniconda
FROM continuumio/miniconda3

# Instalar dependencias del sistema necesarias para construir paquetes
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libffi-dev \
    libssl-dev \
    libbz2-dev \
    libsqlite3-dev \
    zlib1g-dev \
    && apt-get clean

# Establece el directorio de trabajo
WORKDIR /app

# Crear el entorno Conda con Python 3.11.6 desde conda-forge
RUN conda create -n environment_proyecto_aplicado python=3.11.6 -c conda-forge -y

# Inicializa Conda en Bash
RUN echo "source /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
    && echo "conda activate environment_proyecto_aplicado" >> ~/.bashrc

# Copiar el código fuente al contenedor
COPY . .

# Cambiar al shell Bash para ejecutar los siguientes comandos
SHELL ["/bin/bash", "-c"]

# Instalar paquetes en bloques para reducir problemas de resolución
RUN source /opt/conda/etc/profile.d/conda.sh && conda activate environment_proyecto_aplicado && \
    pip install \
    langchain langchain_community langchain_chroma langchain_text_splitters \
    && pip install \
    langchain_huggingface sentence-transformers langchain_qdrant qdrant-client \
    && pip install \
    langchain_ollama pypdf langchain_openai fastembed spacy streamlit

# Descargar el modelo spaCy en_core_web_sm
RUN source /opt/conda/etc/profile.d/conda.sh && conda activate environment_proyecto_aplicado && \
    python -m spacy download en_core_web_sm

# Exportar el entorno Conda sin builds para reproducir
RUN source /opt/conda/etc/profile.d/conda.sh && conda activate environment_proyecto_aplicado && \
    conda env export --no-builds > environment_container.yml

# Comando predeterminado para mantener el contenedor activo
CMD ["bash"]