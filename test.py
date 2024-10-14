import pytest
from api_json import app

#fixtures para el cliente de pruebas
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Prueba para el endpoint POST /users
def test_create_user(client):
    # Simula una petición POST para crear un usuario
    response = client.post('/create_user', json={'nombre':'pepe','edad':'26','id':'4'})
    assert response.status_code == 201
    data = response.get_json()
    print('response',data)
    assert data['message'] == 'Creado correctamente'
    #assert data['usuarios']['nombre'] == 'pedro'


def test_get_usuario(client):
    response =client.get('/users')
    assert response.status_code==200
    data=response.get_json()
    assert len(data)==4
    assert data[3]['nombre']=='pepe'

def test_get_usuarios_id(client):
    response =client.get('/getid/2')
    assert response.status_code==200
    data=response.get_json()
    print('datos',data)
    assert data['usuarios']['nombre']=='pepe'