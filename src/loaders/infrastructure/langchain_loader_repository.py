from src.loaders.domain import LoaderRepository,DocumentValue
from langchain_community.document_loaders import PyPDFLoader

class LangchainLoaderRepository(LoaderRepository):
    def load_file(self, path: str)->list[DocumentValue]:
        loader = PyPDFLoader(file_path=path)
        docs = loader.load()
        domain_docs = [
            DocumentValue(content=doc.page_content, metadata=doc.metadata)
            for doc in docs
        ]
        return domain_docs
