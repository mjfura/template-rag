import streamlit as st

from src.helpers.benchmarking import evaluate_retrievers
from src.config import data_ground_truth
from .main_instances import application, knowledge_base_use_case


def launch_app() -> None:
    menu = st.sidebar.selectbox(
        "Navegación", ["Inicio", "Base del Conocimiento", "Retrievers", "Benchmarking"]
    )

    # Mostrar contenido según la selección
    if menu == "Inicio":
        st.title("Proyecto Final - RAG")
        st.write(
            "En esta aplicación se podrá cargar archivos PDF, preprocesarlos y crear la base del conocimiento. Además, se podrán realizar consultas a los dos Retrievers: Básico y Avanzado."
        )
        st.write(
            "Por último, se podrá realizar un benchmarking entre ambos Retrievers."
        )
        st.write("Para navegar, seleccione una opción en el menú lateral.")
    elif menu == "Base del Conocimiento":
        st.title("Creación de Base del Conocimiento")
        st.write(
            "En esta sección se cargarán los archivos PDF y se preprocesarán para crear la base del conocimiento."
        )
        uploaded_files = st.file_uploader(
            "Cargar archivo PDF", type=["pdf"], accept_multiple_files=True
        )
        if uploaded_files is not None:
            if st.button("Cargar"):
                with st.spinner("Generando chunks..."):
                    ids = knowledge_base_use_case.generate_knowledge_base(
                        uploaded_files
                    )
                st.success("Chunks generados!")
                st.write("ids de los chunks generados:")
                st.write(ids)
    elif menu == "Retrievers":
        st.title("Ejecutar Retrievers")
        st.write("En esta sección se ejecutarán los dos Retrievers: Básico y Avanzado.")
        st.subheader("Retriever Básico")
        query = st.text_input("Ingrese una consulta:")
        if st.button("Buscar"):
            st.write("Buscando documentos...")
            response = application.pipeline_rag(query)
            st.write("Respuesta:")
            st.write(response)

        st.subheader("Retriever Avanzado")
        question = st.text_input("Ingrese una pregunta:")
        if st.button("Evaluar"):
            st.write("Evaluando pregunta...")
            answer = application.pipeline_rag_advanced(question)
            st.write("Respuesta:")
            st.write(answer)
            st.write("----")

        st.subheader("Chat")
        if "history_messages" not in st.session_state:
            st.session_state["history_messages"] = []
        messages = st.container(height=500)
        if prompt := st.chat_input("Escribe una consulta..."):
            for message in st.session_state["history_messages"]:
                messages.chat_message(message["author"]).write(message["message"])
            messages.chat_message("user").write(prompt)
            basic_response = application.pipeline_rag(prompt)
            advanced_response = application.pipeline_rag_advanced(prompt)
            messages.chat_message("assistant").write(
                f"**Basic Retriever:** {basic_response}"
            )
            messages.chat_message("assistant").write(
                f"**Advanced Retriever:** {advanced_response}"
            )
            st.session_state["history_messages"].append(
                {"author": "user", "message": prompt}
            )
            st.session_state["history_messages"].append(
                {"author": "assistant", "message": f"Basic Retriever: {basic_response}"}
            )
            st.session_state["history_messages"].append(
                {
                    "author": "assistant",
                    "message": f"Advanced Retriever: {advanced_response}",
                }
            )

    elif menu == "Benchmarking":
        st.title("Benchmarking")
        st.write(
            "Para realizar la comparación entre ambos retrievers, puede presionar el botón 'Realizar Benchmarking'."
        )
        if st.button("Realizar Benchmarking"):
            with st.spinner("Evaluando Retrievers..."):
                df_result_basic, df_result_advanced = evaluate_retrievers(
                    application, data_ground_truth
                )
            st.write("Resultados del Retriever Básico")
            st.write(df_result_basic)
            st.write("----")
            st.write(
                "Mean Faithfulness: ", round(df_result_basic["faithfulness"].mean(), 4)
            )
            st.write(
                "Mean Answer relevancy: ",
                round(df_result_basic["answer_relevancy"].mean(), 4),
            )
            st.write(
                "Mean Context recall: ",
                round(df_result_basic["context_recall"].mean(), 4),
            )
            st.write(
                "Mean Context precision: ",
                round(df_result_basic["context_precision"].mean(), 4),
            )
            st.write("Resultados del Retriever Avanzado")
            st.write(df_result_advanced)
            st.write("----")
            st.write(
                "Mean Faithfulness: ",
                round(df_result_advanced["faithfulness"].mean(), 4),
            )
            st.write(
                "Mean Answer relevancy: ",
                round(df_result_advanced["answer_relevancy"].mean(), 4),
            )
            st.write(
                "Mean Context recall: ",
                round(df_result_advanced["context_recall"].mean(), 4),
            )
            st.write(
                "Mean Context precision: ",
                round(df_result_advanced["context_precision"].mean(), 4),
            )
