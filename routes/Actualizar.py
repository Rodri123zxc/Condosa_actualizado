from flask import Blueprint, request, jsonify
from models.casa import Casa
from models.casa_estado import CasaEstado
from utils.db import db

actualizar_bp = Blueprint('actualizar', __name__)

@actualizar_bp.route('/actualizar_estado', methods=['POST'])
def actualizar_estado():
    casa_id = request.json.get('casaId')
    nuevo_estado = request.json.get('nuevoEstado')

    estado = CasaEstado.query.filter_by(descripcion=nuevo_estado).first()
    if estado is None:
        return jsonify({'error': 'El estado proporcionado no existe.'}), 400

    casa = Casa.query.get(casa_id)
    if casa is None:
        return jsonify({'error': 'La casa con el ID proporcionado no existe.'}), 400

    casa.id_estado = estado.id_estado

    try:
        db.session.commit()
        return jsonify({'message': 'Estado de la casa actualizado correctamente.'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al actualizar el estado de la casa.'}), 500

@actualizar_bp.route('/guardar_estado_masivo', methods=['POST'])
def guardar_estado_masivo():
    data = request.get_json()
    casa_ids = data.get('casaIds')
    nuevo_estado = data.get('nuevoEstado')

    if not casa_ids or not nuevo_estado:
        return jsonify({'error': 'IDs de casas o nuevo estado no proporcionados.'}), 400

    try:
        casa_ids = [int(casa_id) for casa_id in casa_ids]

        casas = Casa.query.filter(Casa.id_casa.in_(casa_ids)).all()
        if not casas:
            return jsonify({'error': 'No se encontraron casas con los IDs proporcionados.'}), 400

        estado = CasaEstado.query.filter_by(descripcion=nuevo_estado).first()
        if not estado:
            return jsonify({'error': 'El estado proporcionado no existe.'}), 400

        for casa in casas:
            casa.id_estado = estado.id_estado

        db.session.commit()

        response = {
            'message': 'Estados de las casas guardados exitosamente.'
        }
        return jsonify(response)

    except ValueError:
        return jsonify({'error': 'IDs de casas inválidos.'}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al guardar los estados de las casas.'}), 500
