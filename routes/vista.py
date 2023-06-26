from flask import Blueprint, render_template
from models import Casa, Predio, Propietario, CasaEstado

# Crea una instancia de Blueprint para la vista
vista_bp = Blueprint('vista', __name__)

# Define la ruta principal ("/")
@vista_bp.route('/')
def vista():
    # Obtén la información de las casas y sus relaciones
    casas = Casa.query.join(Predio).join(Propietario).join(CasaEstado).all()

    # Crea una lista para almacenar los datos a mostrar en la tabla
    datos = []

    # Recorre cada casa y agrega los campos deseados a la lista de datos
    for casa in casas:
        dato = {
            'id_casa': casa.id_casa,
            'piso': casa.piso,
            'area': casa.area,
            'descripcion': casa.predio.descripcion,
            'direccion': casa.predio.direccion,
            'nombres': casa.propietario.persona.nombres,
            'estado_casa': casa.casa_estado.descripcion
        }
        datos.append(dato)

    # Renderiza el template "vista.html" con los datos obtenidos
    return render_template('vista.html', datos=datos)
