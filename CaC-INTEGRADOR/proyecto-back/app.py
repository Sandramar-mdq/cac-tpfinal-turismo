#  Importar las herramientas
# Acceder a las herramientas para crear la app web
from flask import Flask, request, jsonify

# Para manipular la DB
from flask_sqlalchemy import SQLAlchemy 

# Módulo cors es para que me permita acceder desde el frontend al backend
from flask_cors import CORS

# Crear la app
app = Flask(__name__)

# permita acceder desde el frontend al backend
CORS(app)


# Configurar a la app la DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost:3306/nombre_de_la_base_de_datos'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:cac1231@localhost:3306/turismo_cac'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear un objeto db, para informar a la app que se trabajará con sqlalchemy
db = SQLAlchemy(app)


# Definir la tabla 
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    telefono = db.Column(db.String(20))
    mail = db.Column(db.String(30))
    foto_dni=db.Column(db.String(400))#aqui guardamos la url a la imabgen 

    def __init__(self,nombre,apellido,telefono,mail,foto_dni):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.apellido=apellido
        self.telefono=telefono
        self.mail=mail
        self.foto_dni=foto_dni
        
        
# Crear la tabla al ejecutarse la app
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        
        
"""# 8. Crear la tabla al ejecutarse la app
with app.app_context():
    db.create_all()"""

# Crear ruta de acceso
# / es la ruta de inicio
@app.route("/")
def index():
    return f'App Web para registrar clientes'

# Crear un registro en la tabla Productos
@app.route("/registro", methods=['POST']) 
def registro():
    # {"nombre": "Felipe", ...} -> input tiene el atributo name="nombre"
    nombre_recibido = request.json["nombre"]
    apellido=request.json['apellido']
    telefono=request.json['telefono']
    mail=request.json['mail']
    foto_dni=request.json['foto_dni']

    nuevo_registro = Cliente(nombre=nombre_recibido,apellido=apellido,telefono=telefono,mail=mail,foto_dni=foto_dni)
    db.session.add(nuevo_registro)
    db.session.commit()

    return "Solicitud de post recibida"
    

# Retornar todos los registros en un Json
@app.route("/clientes",  methods=['GET'])
def clientes():
    # Consultar en la tabla todos los registros
    # all_registros -> lista de objetos
    all_registros = Cliente.query.all()

    # Lista de diccionarios
    data_serializada = []
    
    for objeto in all_registros:
        data_serializada.append({"id":objeto.id, "nombre":objeto.nombre, "apellido":objeto.apellido, "telefono":objeto.telefono, "mail":objeto.mail, "foto_dni":objeto.foto_dni})

    return jsonify(data_serializada)


# Modificar un registro
@app.route('/update/<id>', methods=['PUT'])
def update(id):
    # Buscar el registro a modificar en la tabla por su id
    cliente = Cliente.query.get(id)

    # {"nombre": "Felipe"} -> input tiene el atributo name="nombre"
    nombre = request.json["nombre"]
    apellido=request.json['apellido']
    telefono=request.json['telefono']
    mail=request.json['mail']
    foto_dni=request.json['foto_dni']

    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.telefono=telefono
    cliente.mail=mail
    cliente.foto_dni=foto_dni
    db.session.commit()

    data_serializada = [{"id":cliente.id, "nombre":cliente.nombre, "apellido":cliente.apellido, "telefono":cliente.telefono, "mail":cliente.mail, "foto_dni":cliente.foto_dni}]
    
    return jsonify(data_serializada)

   
@app.route('/borrar/<id>', methods=['DELETE'])
def borrar(id):
    
    # Se busca a la productos por id en la DB
    cliente = Cliente.query.get(id)

    # Se elimina de la DB
    db.session.delete(cliente)
    db.session.commit()

    data_serializada = [{"id":cliente.id, "nombre":cliente.nombre, "apellido":cliente.apellido, "telefono":cliente.telefono, "mail":cliente.mail, "foto_dni":cliente.foto_dni}]

    return jsonify(data_serializada)


if __name__ == "__main__":
    app.run(debug=True)
    