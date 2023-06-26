from flask import Blueprint, request, jsonify
from models import Casa, Predio, Propietario, CasaEstado

# Crea una instancia de Blueprint para la vista
actualizar_bp = Blueprint('actualizar', __name__)

# Define la ruta para actualizar el estado ("/actualizar_estado")
@actualizar_bp.route('/actualizar_estado', methods=['POST'])
def actualizar_estado():
    casa_id = request.json['casaId']
    nuevo_estado = request.json['nuevoEstado']

    # Obtener el id del estado correspondiente al nuevo estado
    estado = CasaEstado.query.filter_by(descripcion=nuevo_estado).first()
    if estado is None:
        return jsonify({'error': 'El estado proporcionado no existe.'}), 400

    # Realizar la actualización en la base de datos
    casa = Casa.query.get(casa_id)
    if casa is None:
        return jsonify({'error': 'La casa con el ID proporcionado no existe.'}), 400

    casa.id_estado = estado.id_estado
    db.session.commit()

    return jsonify({'message': 'Estado de la casa actualizado correctamente.'})
