from app import crear_app
from utils.db import db

app = crear_app()

# Método main
if __name__ == '__main__':
    app.run()
