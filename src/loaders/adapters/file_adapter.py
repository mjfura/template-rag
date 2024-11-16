from streamlit.runtime.uploaded_file_manager import UploadedFile
from src.loaders.domain import FileValue
def create_file_adapter(file: UploadedFile) -> FileValue:
    return FileValue(
        name=file.name,
        size=file.size,
        type=file.type,
        content=file.getbuffer()
    )