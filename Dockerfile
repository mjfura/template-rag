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
    langchain==0.3.7 langchain_community==0.3.5 langchain_chroma==0.1.4 langchain_text_splitters==0.3.2 \
    && pip install \
    langchain_huggingface==0.1.2 sentence-transformers==3.2.1 langchain_qdrant==0.2.0 qdrant-client==1.8.0 \
    && pip install \
    langchain_ollama==0.2.0 pypdf==5.1.0 langchain_openai==0.2.6 fastembed==0.4.1 spacy==3.8.2 streamlit==1.40.0 ragas==0.2.6 tqdm==4.67.0

# Descargar el modelo spaCy en_core_web_sm
RUN source /opt/conda/etc/profile.d/conda.sh && conda activate environment_proyecto_aplicado && \
    python -m spacy download en_core_web_sm

# Exportar el entorno Conda sin builds para reproducir
RUN source /opt/conda/etc/profile.d/conda.sh && conda activate environment_proyecto_aplicado && \
    conda env export --no-builds > environment_container.yml

# Comando predeterminado para mantener el contenedor activo
CMD ["bash"]