from langchain.schema import Document
from src.loaders.domain import DocumentValue

def create_document_adapter(docs:list[DocumentValue])->list[Document]:
    return [Document(page_content=doc.content,metadata=doc.metadata) for doc in docs]