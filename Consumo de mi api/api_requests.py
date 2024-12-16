import requests

# Este archivo se usa para interactuar directamente con la api, organiza las funciones del CRUD (GET, POST, PUT o PATC y DELETE)


BASE_URL = "http://127.0.0.1:8000/api/v1/" # URL dada por django para la api

# GET
def obtener_datos(access_token):
    """
    Realiza una solicitud GET para obtener los datos de la API.
    """
    url = f"{BASE_URL}Programadores/"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200: # Muestra si todo fue correctamente
        return response.json()
    else:
        print("Error al obtener datos:", response.json())
        return None

# POST
def crear_datos(access_token, datos):
    """
    Realiza una solicitud POST para crear un nuevo recurso en la API.
    """
    url = f"{BASE_URL}Programadores/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=datos, headers=headers)
    if response.status_code == 201: # Muesta si todo fue correctamente y que se devolvio o creo un nuevo recurso en la API
        print("Recurso creado:", response.json())
    else:
        print("Error al crear recurso:", response.json())

# PUT o PATCH
def actualizar_datos(access_token, id, nuevos_datos):
    """
    Realiza una solicitud PUT para actualizar un recurso existente en la API.
    """
    url = f"{BASE_URL}Programadores/{id}/"  
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.put(url, json=nuevos_datos, headers=headers)
    if response.status_code == 200: # Muesta si todo fue correctamente
        print("Recurso actualizado:", response.json())
    else:
        print("Error al actualizar recurso:", response.json())


# DELETE
def eliminar_datos(access_token, id):
    """
    Realiza una solicitud DELETE para eliminar un recurso existente en la API.
    """
    url = f"{BASE_URL}Programadores/{id}/"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204: # Muesta si todo fue correctamente y que el usuario no tiene que devolver nada
        print("Recurso eliminado exitosamente.")
    else:
        print("Error al eliminar recurso:", response.json())
