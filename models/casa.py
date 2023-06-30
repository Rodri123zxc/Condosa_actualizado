from utils.db import db

class Casa(db.Model):
    __tablename__ = 'casa'
    id_casa = db.Column(db.Integer, primary_key=True, default=db.text("nextval('id_casa_seq'::regclass)"))
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id_predio'), nullable=True)
    id_estado = db.Column(db.Integer, db.ForeignKey('casa_estado.id_estado'), nullable=False)
    id_predio_mdu = db.Column(db.Integer, nullable=True)
    numero = db.Column(db.SmallInteger, nullable=False)
    piso = db.Column(db.SmallInteger, nullable=True)
    area = db.Column(db.Numeric, nullable=False)
    participacion = db.Column(db.Numeric(6, 2), nullable=True)

    estado = db.relationship('CasaEstado', backref='casas')

    def __init__(self, id_predio, id_estado, id_predio_mdu, numero, piso, area, participacion):
        self.id_predio = id_predio
        self.id_estado = id_estado
        self.id_predio_mdu = id_predio_mdu
        self.numero = numero
        self.piso = piso
        self.area = area
        self.participacion = participacion
