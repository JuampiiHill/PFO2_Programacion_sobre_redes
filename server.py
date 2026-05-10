from flask import Flask, request, jsonify
import bcrypt
from db import conectar_db, create_table, new_user, find_user

app = Flask(__name__)

conn, cursor = conectar_db()
create_table(cursor)
conn.close()

@app.route("/")
def inicio():
    return "Hola mundo"

@app.route("/registro", methods=["POST"])
def registro():

    conn, cursor = conectar_db()

    try:
        data = request.json

        name = data["name"]
        lastname = data["lastname"]
        username = data["username"]
        password = data["password"]

        if not name or not lastname or not username or not password:
            return jsonify({"error": "Todos los campos deben ser obligatorios"})
        
        existing_user = find_user(cursor, username)

        if existing_user:
            return jsonify({"error": "El usuario ya existe"})
        else:
        
            password_bytes = password.encode("utf-8") #convertir texto a bytes
            salt = bcrypt.gensalt() #generar "salt" para evitar hashes repetidos
            password_hash = bcrypt.hashpw(password_bytes, salt) #hash real
            password_hash = password_hash.decode("utf-8")

            created = new_user(cursor, conn, name, lastname, username, password_hash)

            if created:
                return jsonify({"message": "Usuario creado exitosamente"})
            else:
                return jsonify({"error": "El usuario ya existe"})


    
    except Exception as e:
        return jsonify({"error": str(e)})
    
    finally:
        conn.close()


@app.route("/login", methods=["POST"])
def ingresar():

    conn, cursor = conectar_db()

    try:
        data = request.json
        user = data["username"]
        password = data["password"]

        if not user or not password:
            return jsonify({"error": "Todos los campos son obligatorios"})
    
        user_db = find_user(cursor, user)

        if not user_db:
            return jsonify({"error": "Usuario no encontrado"})
    
        hash = user_db[4]

        password_bytes = password.encode("utf-8")
        hash_bytes = hash.encode("utf-8")

        if bcrypt.checkpw(password_bytes, hash_bytes):

            return jsonify({"message": f"Bienvenido {user_db[1]}"})
        
        else:
            return jsonify({"error": "Usuario o contrasenia incorrecta"})
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
    finally:
        conn.close()

@app.route("/tareas", methods=["GET"])
def tareas():
    return "<h1>Bienvenido</>"


if __name__ == "__main__":
    app.run(debug=True)