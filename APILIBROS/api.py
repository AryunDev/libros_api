# API - Es un lugar para disponibilizar recursos y o funcionalidades

# 1 Objetivo - Crear una API que que facilita la consulta, creacion, edicion y eliminacion de libros

# 2 URL BASE - por ahora localhost.com
# 3 Endpoints - 
    # - localhost/libros(get)
    # - localhost/libros/id (GET)
    # - localhost/libros/id (PUT)
    # - localhost/libro/id (DELETE)
# 4 Cuales recursos

from flask import Flask, jsonify, request

api = Flask(__name__)

libros = [
    {
        'id': 1,
        'titulo': 'El señor de los anillos - La Sociedad del anillo',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter y la Piedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atómicos'
    }
]

# Consultar(todos)
@api.route('/libros', methods=['GET'])
def obtener_libros():
    return jsonify(libros)

# Consultar(id)
@api.route('/libros/<int:id>', methods=['GET'])
def obtener_libro_por_id(id):
    for libro in libros:
        if libro.get(id) == id:
            return jsonify(libro)
# Crear
@api.route('/libros', methods=['POST'])
def agregar_nuevo_libro():
    nuevo_libro = request.get_json()
    libros.append(nuevo_libro)

    return jsonify(libros)
# Editar
@api.route('/libros/<int:id>', methods=['PUT'])
def editar_libro_por_id(id):
    libro_alterado = request.get_json()
    for indice,libro in enumerate(libros):
        if libro.get('id') == id:
            libros[indice].update(libro_alterado)
            return jsonify(libros[indice])
# Eliminar
@api.route('/libros/<int:id>',methods=['DELETE'])
def excluir_libro(id):
    for indice, libro in enumerate(libros):
        if libro.get('id') == id:
            del libros[indice]
api.run(port=5000, host='localhost', debug=True)