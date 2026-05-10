import requests

HOST = "localhost"
PORT = 5000
url_register = f"http://{HOST}:{PORT}/registro"
url_in = f"http://{HOST}:{PORT}/login"
url_task = f"http://{HOST}:{PORT}/tareas"

data = {
    "name": "Juan Pablo",
    "lastname": "Hillcoat",
    "username": "juan",
    "password": "1234"
}

response = requests.post(url_register, json=data)
print(response.text)

response = requests.post(url_in, json=data)
print(response.text)

response = requests.post(url_task, json=data)
print(response.text)
    
