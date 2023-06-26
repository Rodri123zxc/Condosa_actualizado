from utils.db import db
class Predio(db.Model):
    id_predio = db.Column(db.Integer, primary_key=True)
    id_tipo_predio = db.Column(db.Integer,db.ForeignKey('tipo_predio.id_tipo_predio'))
    descripcion = db.Column(db.String(80))
    ruc = db.Column(db.String(20))
    telefono = db.Column(db.String(12))
    correo = db.Column(db.String(80))
    direccion = db.Column(db.String(100))
    idubigeo = db.Column(db.String(6),db.ForeignKey('ubigeo.idubigeo'))
    id_persona = db.Column(db.Integer,db.ForeignKey('persona.id_persona'))

    def __init__(self, id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo, id_persona):
        self.id_tipo_predio = id_tipo_predio
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.idubigeo = idubigeo
        self.id_persona = id_persona
