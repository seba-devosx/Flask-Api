
from app import db
##se debe importar db desde app
##se debe definir un nombre para el modelo y como se importo db
## se debe llamar para indicar el nombre de las columna y el tipo de datos
##  algunos valores se les indica que unique ya que son valores que no se deben repetir
## y que el nullable este en false es que no permite valores nulos 
## se le agrega un funcion, la cual se ejecutara uba vez se ejecute el modelo

class Usuarios(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(10),nullable=False)
    #alias_usuarios=db.Column(db.String(10),unique=True,nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
