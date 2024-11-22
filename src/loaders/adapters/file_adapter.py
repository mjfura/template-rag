from streamlit.runtime.uploaded_file_manager import UploadedFile
from src.loaders.domain import FileValue


def create_file_adapter(file: UploadedFile) -> FileValue:
    """
    Converts a Streamlit UploadedFile object into a FileValue object.

    Args:
        file (UploadedFile): The Streamlit UploadedFile object to be converted.
    Returns:
        FileValue: A FileValue object created from the given UploadedFile.
    """
    return FileValue(
        name=file.name, size=file.size, type=file.type, content=file.getbuffer()
    )
