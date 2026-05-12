PFO 2 - Gestión de usuarios 

Proyecto académico, API desarrollado con Flask que permite registrar usuarios, loguearse y gestionar datos en una base de datos SQLite con almacenamiento seguro de contraseñas utilizando bcrypt

## Tecnologías usadas

- Python
- Flask
- SQLite
- bcrypt
- requests

## Estructura del proyecto

- server.py - API Flask (endpoints)
- db.py - conexion y operacion con SQLite
- cliente.py - cliente de prueba

## Instalación y ejecución

### 1. Clonar el respositorio

git clone https://github.com/JuampiiHill/PFO2_Programacion_sobre_redes

### 2. Instalar dependencias

pip install flask bcrypts requests

### 3. Ejecución del servidor

python server.py

El servidor se ejecutará en http://localhost:5000

### 4. Prueba con cliente

python client.py

Esto realiza pruebas automáticas de registro e inicio de sesión

## Las contraseñas no se almacenan en texto palno. Se utiliza bycrypt para generar hashes seguros con salt

## Notas
La base de datos SQLite se crea automáticamente al iniciar el servidor.
El usuario debe tener todos los campos completos para registrarse
EL username debe ser único

## Proyecto realizado como parte de la PFO 2 - Sistema de Gestión de Tareas con API y Base de datos

## Capturas de pantallas

### Servidor funcionando
    screenshots/server.png

### Cliente
    screenshots/cliente.png

### Navegador web
    screenshots/navegador.png

## Respuestas conceptuales

### ¿Por qué hashear contraseñas?

Las contraseñas se hashean para evitar almacenarlas en texto plano. 
De esta forma si la base de datos es comprometida las contraseñas reales de los usuarios no quedan expuestas

### Ventajas de usar SQLite

No requiere instalar un servidor adicional y es ideal para estos tipos de proyectos. Además es liviana y facil de integrar con Python.