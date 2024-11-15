import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st

def header():
    st.title("Actividad 01")
    st.subheader("Carga de Documentos")
    st.write("En esta sección se cargará un archivo pdf, se preprocesará y se guardará en un Bucket. Detallaremos todo el flujo paso a paso.")


header()


uploaded_file = st.file_uploader("Cargar archivo PDF", type=["pdf"])
if uploaded_file is not None:
    st.write("Archivo cargado exitosamente.")
    st.write("Nombre del archivo: ", uploaded_file.name)
    st.write("Tipo de archivo: ", uploaded_file.type)
    st.write("Tamaño del archivo: ", uploaded_file.size)
    st.write("Guardando archivo en un Bucket...")
    
    # Crear la carpeta /bucket si no existe
    bucket_folder = os.path.join(os.path.dirname(__file__), "bucket")
    if not os.path.exists(bucket_folder):
        os.makedirs(bucket_folder)

    # Guardar el archivo en la carpeta /bucket
    with open(os.path.join(bucket_folder, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    
    st.write("Archivo guardado en la carpeta /bucket.")

    # Guardar archivo en un Bucket
    st.write("Archivo guardado exitosamente.")

