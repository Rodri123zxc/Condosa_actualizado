from utils.db import db
from models.persona import Persona

class Predio(db.Model):
    __tablename__ = 'predio'
    id_predio = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(80))
    ruc = db.Column(db.String(20))
    telefono = db.Column(db.String(12))
    correo = db.Column(db.String(80))
    direccion = db.Column(db.String(100))
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    id_tipo_predio = db.Column(db.Integer, db.ForeignKey('tipo_predio.id_tipo_predio'))

    def __init__(self, descripcion, ruc, telefono, correo, direccion, id_persona, id_tipo_predio):
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.id_persona = id_persona
        self.id_tipo_predio = id_tipo_predio
