from utils.db import db
from models.persona import Persona

class Solicitante(db.Model):
    __tablename__ = 'solicitante'
    id_solicitante = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    telefono = db.Column(db.Integer)
    correo = db.Column(db.String(80))



def __init__(self, id_solicitante, id_persona, telefono, correo):
        self.id_solicitante = id_solicitante
        self.id_persona = id_persona
        self.telefono = telefono
        self.correo = correo
        