import os
from src.loaders.domain import BucketRepository
from src.config import BUCKET_PATH

class LocalRepository(BucketRepository):
    def upload(self, file)->str:
        # Crear la carpeta /bucket si no existe 
        if not os.path.exists(BUCKET_PATH):
            os.makedirs(BUCKET_PATH)

        # Guardar el archivo en la carpeta /bucket
        file_path = os.path.join(BUCKET_PATH, file.name)
        with open(file_path, "wb") as f:
           f.write(file.content)
        
        return file_path
    
        
        