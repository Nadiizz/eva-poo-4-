import requests

# Este archivo autentica los tokens para el uso del programa


BASE_URL = "http://127.0.0.1:8000/api"

def obtener_token(username, password):  # Esto obtiene un token luego de que los datos del usuario hayan sido validados
    url = f"{BASE_URL}/token/" # La URL de donde toma los tokens
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)
    if response.status_code == 200: 
        tokens = response.json()
        print("Inicio de sesión exitoso.") # una vez iniciada la sesion muesta este comentario
        return tokens['access']
    else:
        print("Error al iniciar sesión:", response.json()) # Si llega a haber algun error de tipeo se muestra el error que tuvo
        return None 
