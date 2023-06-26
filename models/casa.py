from utils.db import db
class Casa(db.Model):

    id_casa = db.Column(db.Integer, primary_key=True)
    id_predio = db.Column(db.Integer,db.ForeignKey('predio.id_predio'))
    id_estado = db.Column(db.Integer,db.ForeignKey('casa_estado.id_estado'))
    id_predio_mdu = db.Column(db.Integer,db.ForeignKey('predio_mdu.id_predio_mdu'))
    numero = db.Column(db.SMALLINT)
    piso = db.Column(db.SMALLINT)
    area = db.Column(NUMERIC)
    participacion = db.Column(NUMERIC(6,2))
 
    def __init__(self, id_casa, id_predio, id_estado, id_predio_mdu, numero, piso, area, participacion):
        self.id_casa = id_casa
        self.id_predio = id_predio
        self.id_estado = id_estado
        self.id_predio_mdu = id_predio_mdu
        self.numero = numero
        self.piso = piso
        self.area = area
        self.participacion = participacion