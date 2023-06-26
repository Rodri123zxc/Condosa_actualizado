from utils.db import db
class TipoPredio(db.Model):
    id_tipo_predio = db.Column(db.Integer, primary_key=True)
    nombre_predio = db.Column(db.String)

    def __init__(self, id_tipo_predio, nombre_predio):
        self.id_tipo_predio = id_tipo_predio
        self.nombre_predio = nombre_predio
