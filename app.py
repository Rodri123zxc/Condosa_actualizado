from flask import Flask
from utils.config import Config
from utils.db import db

def crear_app():
    app = Flask(__name__)
    # CARGAR CONFIGURACION
    app.config.from_object(Config)

    # IMPORTAR BLUEPRINTS
    from routes.Actualizar import actualizar_bp
    from routes.vista import vista_bp
    from routes.vista2 import vista2_bp

    # REGISTRAR BLUEPRINTS
    app.register_blueprint(actualizar_bp)
    app.register_blueprint(vista_bp, url_prefix='')
    app.register_blueprint(vista2_bp)

    # VINCULAR EL DB CON NUESTRA APP
    db.init_app(app)

    return app

# INSTANCIAR LA APP
app = crear_app()

@app.route('/reniec')
def reniec():
    return render_template('reniec.html')

# METODO MAIN
if __name__ == '__main__':
    app.run()
