
from flask import jsonify,Blueprint

api_route = Blueprint('api_route', __name__)

@api_route.route('/users',methods=['GET'])
def get_usuarios():
    return jsonify('Hola'),200



