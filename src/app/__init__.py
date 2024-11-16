import streamlit as st
from src.loaders.app import loader_use_case
from src.loaders.adapters import create_file_adapter
def header():
    st.title("Actividad 01")
    st.subheader("Carga de Documentos")
    st.write("En esta sección se cargará un archivo pdf, se preprocesará y se guardará en un Bucket. Detallaremos todo el flujo paso a paso.")


def launch_app():
    header()
    uploaded_file = st.file_uploader("Cargar archivo PDF", type=["pdf"])
    if uploaded_file is not None:
        st.write("Archivo cargado exitosamente.")
        st.write("Nombre del archivo: ", uploaded_file.name)
        st.write("Tipo de archivo: ", uploaded_file.type)
        st.write("Tamaño del archivo: ", uploaded_file.size)
        st.write("Guardando archivo en un Bucket...")
        file = create_file_adapter(uploaded_file)
        loader_use_case.upload_to_bucket(file)
        st.write("Archivo guardado en la carpeta /bucket.")
