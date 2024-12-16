from auth import obtener_token
from api_requests import obtener_datos, crear_datos, actualizar_datos, eliminar_datos

def main():
    print("Bienvenido a la lista de programadores")
    access_token = None, None

    while True: # Menú de opciones
        print("\nMenú:")
        print("1. Iniciar sesión")
        print("2. Obtener datos")
        print("3. Crear nuevo recurso")
        print("4. Actualizar recurso existente")
        print("5. Eliminar recurso")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1": # Esta opcion es para iniciar sesión
                username = input("Usuario: ")
                password = input("Contraseña: ")
                access_token = obtener_token(username, password) # Esto solicita un token si es que se ingresa los datos del SuperUser
                if not access_token:
                    print("No se pudo iniciar sesión. Verifica tus credenciales.")

            elif opcion == "2": # opcion para obtener los datos (GET)
                if not access_token:
                    print("Por favor, inicia sesión primero.") # Esta respuesta la da por si no se inicio sesión
                else:
                    try:
                        datos = obtener_datos(access_token) # Esto es para ver los datos que estan en la api (GET)
                        if datos:
                            print("Datos obtenidos:", datos)
                    except Exception as e:
                        print("Error al obtener datos:", e)

            elif opcion == "3": # opcion para agregar los datos (POST) 
                if not access_token:
                    print("Por favor, inicia sesión primero.")
                else:
                    try:
                        nombre_completo = input("Ingrese el nombre completo: ") 
                        apodo = input("Ingrese el apodo: ")
                        edad = int(input("Ingrese la edad: "))
                        datos = {
                            "nombre_completo": nombre_completo,
                            "apodo": apodo,
                            "edad": edad
                        }
                        crear_datos(access_token, datos)
                    except Exception as e:
                        print("Error al crear recurso:", e)

            elif opcion == "4": # Opcion para editar los datos (PUT o PATCH)
                if not access_token:
                    print("Por favor, inicia sesión primero.")
                else:
                    try:
                        id = input("ID del recurso a actualizar: ")
                        nombre_completo = input("Nuevo nombre completo: ")
                        apodo = input("Nuevo apodo: ")
                        edad = int(input("Nueva edad: "))
                        nuevos_datos = {
                            "nombre_completo": nombre_completo,
                            "apodo": apodo,
                            "edad": edad
                        }
                        actualizar_datos(access_token, id, nuevos_datos)
                    except Exception as e:
                        print("Error al actualizar recurso:", e)

            elif opcion == "5": # Opcion para eliminar los datos (DELETE)
                if not access_token:
                    print("Por favor, inicia sesión primero.")
                else:
                    try:
                        id = input("ID del recurso a eliminar: ")
                        eliminar_datos(access_token, id)
                    except Exception as e:
                        print("Error al eliminar recurso:", e)

            elif opcion == "6": # Opcion para cerrar sesion 
                print("¡Adiós!")
                break

            else:
                print("Opción no válida. Intenta de nuevo.") 

        except ValueError as ve:
            print("Error de valor ingresado:", ve) # Parte del try para que no se caiga el codigo
        except Exception as e:
            print("Ha ocurrido un error inesperado:", e) # Lo mismo de arriba

if __name__ == "__main__":
    main()
