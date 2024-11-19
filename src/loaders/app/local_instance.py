from src.loaders.infrastructure import LocalRepository,LangchainLoaderRepository
from src.loaders.use_cases import LoaderUseCase
from src.loaders.adapters import create_file_adapter,create_document_adapter
from streamlit.runtime.uploaded_file_manager import UploadedFile
from langchain.schema import Document


local_repository = LocalRepository()
langchain_repository = LangchainLoaderRepository()
loader_use_case = LoaderUseCase(langchain_repository,local_repository)

def pipeline_load_file(uploaded_file:UploadedFile)->list[Document]:
    """
    Load a file to the bucket and return the documents.
    
    This function receives an uploaded file, loads it to the bucket, and returns the documents.
    
    Args:
        uploaded_file (UploadedFile): The uploaded file to be loaded.
        
    Returns:
        list[Document]: A list of Langchain Document objects.
    """
    file = create_file_adapter(uploaded_file)
    docs=loader_use_case.upload_to_bucket(file)
    docs = create_document_adapter(docs)
    return docs
