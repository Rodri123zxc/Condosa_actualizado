from flask import Blueprint, render_template, request, jsonify
from models.ubigeo import Ubigeo
from models.persona import Persona
from models.solicitante import Solicitante
from sqlalchemy.orm import joinedload
from sqlalchemy import join
from utils.db import db

vista2_bp = Blueprint('vista2', __name__)  # Cambio de 'vista_bp' a 'vista2_bp'

@vista2_bp.route('/reniec.html')  # Cambio de 'vista_bp.route' a 'vista2_bp.route'
def reniec():  # Cambio de 'index' a 'reniec'
    Personas = db.session.query(
        Persona.ndocumento, Persona.nombres, Persona.apellido_materno, Persona.apellido_paterno,
        Persona.fecha_nacimiento, Persona.direccion, Ubigeo.departamento, Ubigeo.provincia, Ubigeo.distrito,
        Solicitante.telefono, Solicitante.correo
    ).select_from(
        join(Persona, Solicitante, Persona.id_persona == Solicitante.id_solicitante)
        .join(Ubigeo, Ubigeo.idubigeo == Persona.idubigeo)
    ).all()

    datos1 = []
    for ndocumento, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, direccion, departamento, provincia, distrito, telefono, correo in Personas:
        datos1.append({
            'DNI': ndocumento,
            'Nombre': nombres,
            'Apellido Paterno': apellido_paterno,
            'Apellido Materno': apellido_materno,
            'Fecha de nacimiento': fecha_nacimiento,
            'Direccion': direccion,
            'Departamento': departamento,
            'Provincia': provincia,
            'Distrito': distrito,
            'Telefono': telefono,
            'Correo': correo
        })

    return render_template('reniec.html', datos1=datos1)
