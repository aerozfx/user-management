from flask import Flask, request
import json
from model.UserRepository import UserRepository

userRepository = UserRepository()

app = Flask(__name__)

app.secret_key = 'clave_secreta_flask'
app.config = {**app.config, "MYSQL_HOST": "localhost", "MYSQL_user": "root", "MYSQL_PASSWORD": "rootroot", "MYSQL_DB": "datos_usuarios"}

# Ruta para ver los registros de la BD
# OK 
@app.get('/users')
def retrieve_user_data():
    users = userRepository.getUsers()
    return users

@app.post('/users')
def create_user():
    # TODO: Create an actual user
    return 201

@app.delete('/user/<user_id>')
def delete_user_by_id(user_id: str):
	return userRepository.delete_user(user_id)

# Ruta para editar a los usuarios existentes
# OK
@app.put('/user/<user_id>')
def edit_user_by_id(user_id: str):
    # Editamos los valores que ya tenemos del usuario
    if request.method == 'POST':
        email = request.form['email']
        nombre = request.form['nombre'] 
        apellidos = request.form['apellidos']
        contrasena = request.form['contrasena']
        telefono = request.form['telefono']
        edad = request.form['edad']

        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE usuarios SET email = %s, nombre = %s, apellidos = %s, contrasena = %s, telefono = %s, edad = %s WHERE id = %s', (email, nombre, apellidos, contrasena, telefono, edad, user_id))
        cursor.connection.commit()
        return 200

        
    cursor= mysql.connection.cursor()
    cursor.execute(f'SELECT * FROM usuarios WHERE id = {user_id}')
    usuario = cursor.fetchall()

    return render_template('editar_usuario.html', usuario = usuario[0])
