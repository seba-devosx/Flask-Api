from flask import Flask,request,jsonify
import json
from flask_cors import CORS


app=Flask(__name__)

CORS(app)

###Nota
## api funcionando con un array de objetos,con las funciones basicas de un crud
## ademas intrega cors para poder usarlo con react
## ya que al estar disponibles en distintos puertos se necesita cors para establecer la conexion
usuarios=[
    {'nombre':'sebastian', 'edad':'26','id':'1'},
    {'nombre':'diego','edad':'26','id':'2'},
    {'nombre':'pedro','edad':'26','id':'3'}
]

#endpoit para obener los usuarios

@app.route('/users',methods=['GET'])
def get_usuarios():
    return jsonify(usuarios),200

@app.route('/getid/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    print(user_id)
    find_usuario=''
    for usuario in usuarios:
        if usuario['id']==user_id:
            print(usuario)
            find_usuario= jsonify(usuario),200
        else:
            None
    if find_usuario:
        return find_usuario
    else:
        return jsonify({'error': 'User not found'}), 404
    
    #este codigo contiene un ciclo for y en un if en una linea, ademas de retornar none
    #si el valor no se encuentra
    # usuario=next((user for user in usuarios if user['id']==user_id),None)
    # print(usuario)
    # if usuario:
    #     return jsonify(usuario)
    # else:
    #    return jsonify({'error': 'User not found'}), 404

@app.route('/delete_user/<int:user_id>',methods=['GET'])
def delete_user(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuarios.remove(usuario)
            return jsonify(usuarios),200

    return jsonify({'error':'User not found'}),404

@app.route('/create_user', methods=['POST'])
def create_user():
    #print(request.json)
    #request.json permite la lectura de los datos enviados desde el post
    new_usuario = request.json
    for usuario in usuarios:
        if usuario['id']== new_usuario['id']:
            return jsonify({"message": "Usuario ya existe", "status": "error"}),400

    usuarios.append(new_usuario)
    return  jsonify({"message": "Creado correctamente", "status": "ok"}),201
           
    #retornamos la lista de usuarios y el codigo de respuesta 
    # que en este caso es un 201
  

@app.route('/modify_user/<int:user_id>',methods=['PUT'])
def modify_usr(user_id):
    for usuario in usuarios:
        if usuario['id']==user_id:
            #de esta forma se actualizarn cada uno de los campos
            #de manera automatica, si especificar onde quieres que se aplique el cambio
            usuario.update(request.json)
            return jsonify(usuario),200
        
            # de esta forma se actualizara cada uno de los cammpos
            #espcificando os valores 
            #usuario['nombre']=request.json['nombre']
            #usuario['edad']=request.json['edad']
            
        
    return jsonify({'error':'User not found'}),404 
            



if __name__ == '__main__':
    app.run(debug=True)