from src.loaders.domain import LoaderRepository, DocumentValue
from langchain_community.document_loaders import PyPDFLoader


class LangchainLoaderRepository(LoaderRepository):
    """
    A repository that loads documents from a file using the PyPDFLoader from the Langchain Community package.

    This class implements the LoaderRepository abstract class from the domain layer.
    """

    def load_file(self, path: str) -> list[DocumentValue]:
        """
        Loads a file and returns a list of DocumentValue objects.

        This method receives a path to a file and returns a list of DocumentValue objects. Each DocumentValue object represents a page of the file.

        Args:
            path (str): The path to the file.

        Returns:
            list[DocumentValue]: A list of DocumentValue objects.
        """
        loader = PyPDFLoader(file_path=path)
        docs = loader.load()
        domain_docs = [
            DocumentValue(content=doc.page_content, metadata=doc.metadata)
            for doc in docs
        ]
        return domain_docs
