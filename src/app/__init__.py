import streamlit as st
from src.loaders.use_cases import LoaderUseCase
from src.loaders.infrastructure import LangchainLoaderRepository, LocalRepository
from src.chunking.use_case import ChankingUseCase
from src.chunking.infrastructure import LangchainChunkingRepository
from src.embedding.infrastructure import SentenceTransformerEmbeddingRepository
from .components import launch_header
from src.application import RAGUseCase, KnowledgeBaseUseCase
from src.vector_store_client.infrastructure import QdrantVectorStoreRepository
from src.chain.infrastructure import OpenAIRepository
from src.embedding.infrastructure import HuggingFaceEmbeddingRepository
from src.retrievers.infrastructure import LangchainRetrieverRepository
from src.cleaner.infrastructure import SpacyRepository
from dotenv import load_dotenv

load_dotenv()

embedding_repository = HuggingFaceEmbeddingRepository()
qdrant_repository = QdrantVectorStoreRepository(
    embedding_repository.get_model(), "archivos_uk"
)
openai_repository = OpenAIRepository()
retriever_repository = LangchainRetrieverRepository(
    qdrant_repository.vector_store.as_retriever(search_kwargs={"k": 10})
)
cleaner_repository = SpacyRepository()
application = RAGUseCase(
    qdrant_repository, retriever_repository, openai_repository, cleaner_repository
)
loader_repository = LangchainLoaderRepository()
bucket_repository = LocalRepository()
loader_use_case = LoaderUseCase(loader_repository, bucket_repository)
chunking_repository = LangchainChunkingRepository()
sentence_embedding_repository = SentenceTransformerEmbeddingRepository()
chunking_use_case = ChankingUseCase(
    chunking_repository, sentence_embedding_repository, cleaner_repository
)
knowledge_base_use_case = KnowledgeBaseUseCase(
    loader_use_case, chunking_use_case, qdrant_repository
)


def launch_app() -> None:
    launch_header(st)
    uploaded_files = st.file_uploader(
        "Cargar archivo PDF", type=["pdf"], accept_multiple_files=True
    )
    if uploaded_files is not None:
        if st.button("Cargar"):
            ids = knowledge_base_use_case.generate_knowledge_base(uploaded_files)
            st.write("ids de los documentos:")
            st.write(ids)

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

    # Inicializar el estado del chat si no existe
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "¡Hola! ¿En qué puedo ayudarte hoy?"}
        ]
    if "user_input" not in st.session_state:
        st.session_state["user_input"] = ""  # Estado inicial de la entrada del usuario

    # Interfaz del chat
    st.title("🤖 Chat con LLM AVANZADO")

    # Mostrar el historial de mensajes
    for message in st.session_state["messages"]:
        if message["role"] == "assistant":
            st.markdown(f"**🤖 Asistente:** {message['content']}")
        else:
            st.markdown(f"**Tú:** {message['content']}")

    # Entrada del usuario
    user_input = st.text_input("Escribe tu mensaje:", key="chat_input")

    # Procesar la entrada cuando se detecte un nuevo mensaje
    if user_input and user_input != st.session_state["last_user_input"]:
        # Actualizar el estado con el nuevo mensaje
        st.session_state["last_user_input"] = user_input
        st.session_state["messages"].append({"role": "user", "content": user_input})

        # Obtener la respuesta del LLM
        response = application.pipeline_rag_advanced(user_input)

        # Agregar la respuesta del asistente al historial
        st.session_state["messages"].append({"role": "assistant", "content": response})

        # Limpiar la entrada del usuario
        st.session_state["last_user_input"] = ""
