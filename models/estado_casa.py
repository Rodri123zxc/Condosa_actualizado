from utils.db import db

class CasaEstado(db.Model):
    id_estado = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(30))

    def __init__(self, id_estado, descripcion):
        self.id_estado = id_estado
        self.descripcion = descripcion
