import os
from src.loaders.domain import LoaderRepository
from src.config import BUCKET_PATH

class LocalRepository(LoaderRepository):
    def upload(self, file):
        # Crear la carpeta /bucket si no existe 
        if not os.path.exists(BUCKET_PATH):
            os.makedirs(BUCKET_PATH)

        # Guardar el archivo en la carpeta /bucket
        with open(os.path.join(BUCKET_PATH, file.name), "wb") as f:
           f.write(file.content)
            
        