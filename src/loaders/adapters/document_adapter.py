from langchain.schema import Document
from src.loaders.domain import DocumentValue

def create_document_adapter(docs:list[DocumentValue])->list[Document]:
    """
    Converts a list of DocumentValue objects into a list of Langchain Document objects.
    Args:
        docs (list[DocumentValue]): A list of DocumentValue objects to be converted.
    Returns:
        list[Document]: A list of Langchain Document objects created from the given DocumentValues.
    """
    return [Document(page_content=doc.content,metadata=doc.metadata) for doc in docs]

def create_document_value_adapter(docs:list[Document])->list[DocumentValue]:
    """
    Converts a list of Langchain Document objects into a list of DocumentValue objects.
    Args:
        docs (list[Document]): A list of Langchain Document objects to be converted.
    Returns:
        list[DocumentValue]: A list of DocumentValue objects created from the given Documents.
    """
    return [DocumentValue(content=doc.page_content,metadata=doc.metadata) for doc in docs]