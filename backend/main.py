from flask import Flask, flash, redirect, url_for, render_template, request
from flask_mysqldb import MySQL

# Creamos las variables necesarias para escribir nuestro JSON

app = Flask(__name__)

app.secret_key = 'clave_secreta_flask'
app.config = {**app.config, "MYSQL_HOST": "localhost", "MYSQL_user": "root", "MYSQL_PASSWORD": "rootroot", "MYSQL_DB": "datos_usuarios"}

mysql = MySQL(app)

# Ruta para añadir usuarios a la BD
# OK
@app.route('/', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        email = request.form['email']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        contrasena = request.form['contrasena']
        telefono = request.form['telefono']
        edad = request.form['edad']
    
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO usuarios VALUES (NULL, %s, %s, %s, %s, %s, %s)', (email, nombre, apellidos, contrasena, telefono, edad))
        cursor.connection.commit()

        flash("Usuario añadido correctamente")
    return render_template('index.html')

# Ruta para ver los registros de la BD
# OK 
@app.route('/usuarios', methods=["GET"])
def retrieve_user_data():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    cursor.close()

    return render_template('datos_usuarios.html', usuarios = usuarios)


# Ruta para borrar a los usuarios deseados
# OK
@app.route('/borrar_usuario/<user_id>')
def delete_user_by_id(user_id: str):
    cursor = mysql.connection.cursor()
    cursor.execute(f'DELETE FROM usuarios WHERE id = {user_id}')
    mysql.connection.commit()
    flash("Usuario eliminado correctamente")

    return redirect(url_for('retrieve_user_data'))

# Ruta para editar a los usuarios existentes
# OK
@app.route('/editar_usuario/<user_id>', methods = ['GET', 'POST'])
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
        return redirect(url_for('retrieve_user_data'))

        
    cursor= mysql.connection.cursor()
    cursor.execute(f'SELECT * FROM usuarios WHERE id = {user_id}')
    usuario = cursor.fetchall()

    return render_template('editar_usuario.html', usuario = usuario[0])

# Podemos pasar parámetros en la ruta de la dirección y mostrarlos por pantalla
# Podemos restringir el tipo de dato que queremos en nuestro argumento con string:parametro o int:parametro o float:parametro

app.run(debug=True)   