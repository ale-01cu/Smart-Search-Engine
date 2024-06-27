import pandas as pd
filename = "C:/Users/Picta/Desktop/Smart-Search-Engine/database/pubs.csv"

class DatabaseModelBase():
    db_filename: str

    def __init__(self) -> None:
        self.db_filename = filename

    @staticmethod
    def get_instance():
        if DatabaseModelBase._instance is None:
            DatabaseModelBase._instance = DatabaseModelBase()
        return DatabaseModelBase._instance
    
    # @staticmethod
    # def __init_subclass__(cls, **kwargs):
    #     print(f"Subclase {cls.__name__} creada")

    # Función para leer el archivo CSV y devuelve un DataFrame
    def read_csv(self, file_name, chunksize=1000):
        return pd.read_csv(file_name, chunksize=chunksize)

    # Función para listar todos los registros
    def list_all(self, page=1):
        chunksize = page * 10**3
        df = self.read_csv(self.db_filename, chunksize=chunksize)
        for i, chunk in enumerate(df):
            if page == i+1:
                chunk['descripcion'] = chunk['descripcion'].astype(str)
                chunk['nombre'] = chunk['nombre'].astype(str)
                return chunk.to_dict('records')

    # Función para obtener un registro por ID
    def get_by_id(self, id):
        df = pd.read_csv(self.db_filename)
        return df.loc[df['id'] == id].to_dict('records')[0]

    # Función para crear un nuevo registro
    def create(self, file_name, data):
        df = self.read_csv(file_name)
        new_row = pd.DataFrame([data], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(file_name, index=False)
        return "Registro creado con éxito"

    # Función para actualizar un registro
    def update(self, file_name, id, data):
        df = self.read_csv(file_name)
        df.loc[df['id'] == id, :] = data
        df.to_csv(file_name, index=False)
        return "Registro actualizado con éxito"

    # Función para eliminar un registro
    def delete(self, file_name, id):
        df = self.read_csv(file_name)
        df = df[df['id'] != id]
        df.to_csv(file_name, index=False)
        return "Registro eliminado con éxito"
        