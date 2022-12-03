import json

from db.database import Database

class EventoDAO:
    def __init__(self):
        self.db = Database(database='programacao', collection='eventos')
        self.collection = self.db.collection

    def create_aula(self, palestra):
        print(palestra)
        res = self.collection.insert_one({"Palestra": palestra.assunto,
                                          "Palestrante": palestra.palestrante.to_string(),
                                          "usuarios": palestra.getListaPresenca()})
        return res.inserted_id

    def read(self, assunto: str):
        return self.collection.find({'Palestra': assunto})

    def update(self, assunto_antigo: str, assunto_novo: str):
        return self.collection.update_one(
            {"Palestra": assunto_antigo},
            {
                "$set": {"Palestra": assunto_novo},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, assunto: str):
        return self.collection.delete_one({"Palestra": assunto})