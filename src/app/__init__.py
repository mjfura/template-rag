import streamlit as st
from src.loaders.app import pipeline_load_file
from src.chunking.app import pipeline_chunking
from src.embedding.app import embeddings_use_case
from src.vector_store_client.app import vector_store_use_case
from .components import launch_header

def launch_app():
    
    launch_header(st)
    uploaded_files = st.file_uploader("Cargar archivo PDF", type=["pdf"], accept_multiple_files=True)
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            st.write("Archivo cargado exitosamente.")
            st.write("Guardando archivo en un Bucket...")
            docs = pipeline_load_file(uploaded_file)
            st.write('Convirtiendo Document a DocumentValue')
            chunks = pipeline_chunking(docs)
            print(f'Chunks: {chunks}')
            st.write('Convirtiendo el primer chunk a embedding...')
            embedding=embeddings_use_case.get_embedding(chunks[0].content)
            st.write("Embedding:")
            st.write(embedding)
            list_ids=vector_store_use_case.add_documents(chunks)
            st.write("Documentos guardados en el Vector Store.")
            st.write("IDs de los documentos:")
            st.write(list_ids)
    
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
    