from flask import Blueprint, render_template, request, jsonify
from models.ubigeo import Ubigeo
from models.persona import Persona
from models.solicitante import Solicitante
from sqlalchemy.orm import joinedload
from sqlalchemy import join
from utils.db import db
from datetime import date
import json

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

    return render_template('reniec.html',datos1=datos1)


def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year
    if hoy.month < fecha_nacimiento.month or (hoy.month == fecha_nacimiento.month and hoy.day < fecha_nacimiento.day):
        edad -= 1
    return edad

@vista2_bp.route('/buscar_persona', methods=['POST'])
def buscar_persona():
    dni = request.form['dni']

    persona = db.session.query(Persona).filter_by(ndocumento=dni).first()

    if persona:
        datos = {
            'encontrada': True,
            'edad': calcular_edad(persona.fecha_nacimiento),
            'fecha_nacimiento': persona.fecha_nacimiento,
            'direccion': persona.direccion,
            'departamento': persona.ubigeo.departamento,
            'provincia': persona.ubigeo.provincia,
            'distrito': persona.ubigeo.distrito,
            'telefono': persona.solicitante.telefono,
            'correo': persona.solicitante.correo
        }
    else:
        datos = {'encontrada': False}

    return jsonify(datos)