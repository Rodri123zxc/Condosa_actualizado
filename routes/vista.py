from flask import Blueprint, render_template, request, jsonify
from models.casa import Casa
from models.predio import Predio
from models.tipo_predio import TipoPredio
from models.casa_estado import CasaEstado
from models.propietario import Propietario
from models.persona import Persona
from sqlalchemy.orm import joinedload
from sqlalchemy import join
from utils.db import db

vista_bp = Blueprint('vista', __name__)

@vista_bp.route('/')
def index():
    casas = db.session.query(
        Casa.id_casa, Casa.numero, Casa.piso, Casa.area,
        Predio.descripcion, TipoPredio.nomre_predio, Predio.direccion,
        Persona.nombres, CasaEstado.descripcion
    ).select_from(
        join(Casa, Predio, Casa.id_predio == Predio.id_predio)
        .join(TipoPredio, Predio.id_tipo_predio == TipoPredio.id_tipo_predio)
        .join(Propietario, Casa.id_casa == Propietario.id_casa)
        .join(Persona, Propietario.id_persona == Persona.id_persona)
        .join(CasaEstado, Casa.id_estado == CasaEstado.id_estado)
    ).all()

    predios = db.session.query(Predio.descripcion).distinct().all()

    datos = []
    for casa_id, numero, piso, area, descripcion_predio, tipo_predio, direccion_predio, nombres_propietario, estado_casa in casas:
        datos.append({
            'id_casa': casa_id,
            'numero': numero,
            'piso': piso,
            'area': area,
            'descripcion_predio': descripcion_predio,
            'tipo_predio': tipo_predio,
            'direccion_predio': direccion_predio,
            'nombres_propietario': nombres_propietario,
            'estado_casa': estado_casa
        })

    return render_template('index.html', datos=datos, predios=predios)
