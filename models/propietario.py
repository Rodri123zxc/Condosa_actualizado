from utils.db import db

class Propietario(db.Model):
    __tablename__ = 'propietario'
    id_propietario = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    id_casa = db.Column(db.Integer, db.ForeignKey('casa.id_casa'))
    id_tipo_predio = db.Column(db.Integer, db.ForeignKey('tipo_predio.id_tipo_predio'))
    porcentaje_propiedad = db.Column(db.Numeric(5, 2))

    persona = db.relationship('Persona', backref='propietarios')
    casa = db.relationship('Casa', backref='propietarios')
    tipo_predio = db.relationship('TipoPredio', backref='propietarios')

    def __init__(self, id_persona, id_casa, id_tipo_predio, porcentaje_propiedad):
        self.id_persona = id_persona
        self.id_casa = id_casa
        self.id_tipo_predio = id_tipo_predio
        self.porcentaje_propiedad = porcentaje_propiedad
