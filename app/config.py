import os 

class Config:

    #ruta de la base de datos sqlite, la ruta puede ser relativa o absoluta 
    BASE_DIR=os.path.abspath(os.path.dirname(__file__))
    #se define la direccion donde se hubicara la base de datos y el nombre que debera tener
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(BASE_DIR,'My_Basedatos.db')}"
    #Desactivar la modificación de seguimiento para mejorar el rendimiento
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    