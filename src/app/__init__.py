import streamlit as st
from src.loaders.app import loader_use_case
from src.loaders.adapters import create_file_adapter,create_document_adapter,create_document_value_adapter
from src.cleaner.app import cleaner_use_case
from src.chunking.app import chunking_use_case
from src.chunking.adapters import create_document_from_chunk_adapter
from src.embedding.app import embeddings_use_case
from src.vector_store_client.infrastructure import QdrantVectorStoreRepository
from src.vector_store_client.use_case import VectorStoreUseCase
def header():
    st.title("Actividad 01")
    st.subheader("Carga de Documentos")
    st.write("En esta sección se cargará un archivo pdf, se preprocesará y se guardará en un Bucket. Detallaremos todo el flujo paso a paso.")


def launch_app():
    qdrant_repository = QdrantVectorStoreRepository(embeddings_use_case.get_model_embedding(),'archivos_uk')
    vector_store_use_case = VectorStoreUseCase(qdrant_repository)
    header()
    uploaded_file = st.file_uploader("Cargar archivo PDF", type=["pdf"])
    if uploaded_file is not None:
        st.write("Archivo cargado exitosamente.")
        st.write("Nombre del archivo: ", uploaded_file.name)
        st.write("Tipo de archivo: ", uploaded_file.type)
        st.write("Tamaño del archivo: ", uploaded_file.size)
        st.write("Guardando archivo en un Bucket...")
        file = create_file_adapter(uploaded_file)
        docs=loader_use_case.upload_to_bucket(file)
        docs = create_document_adapter(docs)
        st.write('Convirtiendo Document a DocumentValue')
        docs_values = create_document_value_adapter(docs)
        chunks = chunking_use_case.get_chunks(docs_values)
        chunks_as_documents = create_document_from_chunk_adapter(chunks)
        print(f'Chunks: {chunks_as_documents}')
        text_example = 'Hi, this is an example for apply a cleaning process to a text.'
        st.write("Texto de ejemplo:")
        st.write(text_example)
        text_cleaned = cleaner_use_case.clean_text(text_example)
        st.write("Texto limpio:")
        st.write(text_cleaned)
        st.write('Convirtiendo texto a embeddings...')
        embedding=embeddings_use_case.get_embedding(text_cleaned)
        st.write("Embedding:")
        st.write(embedding)
        list_ids=vector_store_use_case.add_documents(chunks)
        st.write("Documentos guardados en el Vector Store.")
        st.write("IDs de los documentos:")
        st.write(list_ids)
        st.write("Archivo guardado en la carpeta /bucket.")
    
    st.subheader("Búsqueda de Documentos")
    query = st.text_input("Ingrese una consulta:")
    if st.button("Buscar"):
        st.write("Buscando documentos...")
        documents = vector_store_use_case.search(query)
        st.write("Documentos encontrados:")
        for document in documents:
            st.write(document.content)
            st.write(document.metadata)
            st.write("----")