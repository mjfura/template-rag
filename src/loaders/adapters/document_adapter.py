from langchain.schema import Document
from src.loaders.domain import DocumentValue

def create_document_adapter(docs:list[DocumentValue])->list[Document]:
    return [Document(page_content=doc.content,metadata=doc.metadata) for doc in docs]

def create_document_value_adapter(docs:list[Document])->list[DocumentValue]:
    return [DocumentValue(content=doc.page_content,metadata=doc.metadata) for doc in docs]