from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.routes import api_route
# se inicia la instanci sqlalchemy
db=SQLAlchemy()
migrate=Migrate()

def create_app():
    # se inicia flask
    app=Flask(__name__)
    #los cors son para poder disponibilizar la conexion en purtos diferentes
    CORS(app)
    # se indica de que archivo app debe tomar la configuracion para la base de datos
    app.config.from_object('app.config.Config')
    #se inicia la creacion de la base de datos cuando se inicia la app
    db.init_app(app)
    #se genera migracion para la app de la base de datos
    migrate.init_app(app,db)
    #se registra la ruta para que pueda ser detectada
    app.register_blueprint(api_route)
    #se retorna la app 
    return app