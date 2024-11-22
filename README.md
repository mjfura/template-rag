# Actividad 01

## Descripción
Este programa permite al usuario subir uno o varios archivos PDF y mediante un pipeline RAG extraer chunks de texto de los archivos, luego almacenarlos en una DB vectorial (Qdrant) y finalmente devolver los ids de el total de chunks agregados por cada archivo.

También se agregó una interfaz para poder obtener los chunks más cercanos en similitud según una query suministrada por el usuario.

Así mismo, en la carpeta `/data/reglamentacion-uk` estamos adjuntando algunos archivos de prueba para poder hacer algunas pruebas.

## Pipeline
El pipeline está compuesto por los siguientes pasos:
1. **Almacenamiento del archivo en un Bucket**: Se almacena el archivo en un Bucket, en este caso por defecto se guardará localmente en el directorio `/bucket` del proyecto.
2. **Extracción de texto**: Se extrae el texto de cada página del archivo PDF.
3. **Extracción de chunks de texto**: Se extraen los chunks de texto en base a un enfoque semántico.
4. **Almacenamiento de los chunks en Qdrant**: Se almacenan los chunks en una DB vectorial (Qdrant).
5. **Obtención de los ids de los chunks**: Se obtienen los ids de los chunks almacenados en Qdrant.
6. **Obtención de los chunks más cercanos en similitud**: Se obtienen los chunks más cercanos en similitud a una query suministrada por el usuario.

## Instrucciones para ejecutar el programa usando Docker 
1. Clonar el repositorio
2. Abrir una terminal
3. Navegar a la carpeta del repositorio
4. Ejecutar el siguiente comando para construir la imagen:
```bash
docker compose build
```
5. Ejecutar el siguiente comando para correr el contenedor:
```bash
docker compose up
```
6. Abrir un navegador web y navegar a la dirección `localhost:8501`

## Instrucciones para ejecutar el programa usando Conda (recomendado en caso de querer usar archivos grandes con más de 500 páginas)
1. Clonar el repositorio
2. Abrir una terminal
3. Navegar a la carpeta del repositorio
4. Crear un nuevo ambiente de Conda con el siguiente comando:
```bash
conda env create -f environment.yml
```
Nota: Este comando creará un ambiente llamado `actividad_1`. En caso de tener problemas al crear el ambiente, alternativamente se puede ejecutar el siguiente comando:
```bash
conda env create -f environment.yml -c conda-forge
```
O por último, se puede usar el archivo `environment.yml` para instalar las dependencias manualmente.

5. Activar el ambiente con el siguiente comando:
```bash
conda activate actividad_1
```
6. Ejecutar el siguiente comando para correr el programa:
```bash
streamlit run main_app.py
```
7. Abrir un navegador web y navegar a la dirección que se muestra en la terminal (usualmente `localhost:8501`)

## Arquitectura del programa
El programa está dividido en dos partes: el frontend y el backend. El frontend está hecho en Python usando Streamlit y el backend está hecho usando una clean architecture en Python.
Se están usando las siguientes capas:
- **Domain**: Contiene la lógica de negocio, expresándolas abstractamente agnóstico a la infrastructure que se usará. Algunos de sus componentes son:
  - **Entities**: Contiene las clases que representan las entidades de la aplicación expresadas como interfaces o clases abstractas.
  - **Repositories**: Contiene las interfaces que representan las operaciones que se pueden realizar sobre las entidades de la aplicación expresadas como clases abstractas.
  - **Values**: Contiene las clases concretas de las entidades.
- **Use Cases**: Contiene las clases que representan los casos de uso de la aplicación. Usualmente ocupando los repositorios del dominio para realizar las operaciones de manera agnóstica a la infrastructure.
- **Infrastructure**: Contiene la implementación de los repositorios del domminio usando las librerias que mejor se ajusten a las necesidades de la aplicación.
- **Adapters**: Contiene los métodos que adaptan las clases internas de nuestro Domain a las clases de las librerias que estamos usando (Infrastructure) y viceversa.
- **App**: Contiene la configuración de la aplicación y la inyección de dependencias.
