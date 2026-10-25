import os 
import requests
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
modelo = "gemini-flash-latest"
    
url_base = f"https://generativelanguage.googleapis.com/v1beta/models/"

#Funcion para crear la solicitud
def armar_peticion(pregunta):
    if not pregunta:
        raise ValueError("La pregunta no puede estar vacía")
    url = f"{url_base}{modelo}:generateContent?key={api_key}"
    body = {
        "contents":[ #En la solicitud es contents
            {
                "parts":[
                    {
                        "text":pregunta
                    }
                ]
            }
        ]
    }

    return url,body

#Funcion envia petición
def enviar_peticion(url,body):
    try:
        respuesta = requests.post(url,json=body) #se puede obtener el timeout de la peticion
        
    except requests.exceptions.ConnectionError:
        raise RuntimeError("no se pudo conectar con el servicio, Intenta más tarde")
    except requests.exceptions.Timeout:
        raise RuntimeError("Se agotó el tiempo de espera, intenta más tarde")
    if respuesta.status_code != 200:
        raise RuntimeError(f"Error en la peticion. status code : {respuesta.status_code}")
    
    try:
        return respuesta.json()
    except requests.exceptions.JSONDecodeError:
        raise RuntimeError("La respuesta del servicio no llegó en el formato esperado")   
   
#Funcion procesa y extrae datos
def extraer_texto(datos):
    try:
        return datos["candidates"][0]["content"]["parts"][0]["text"] #Pero en la respuesta es content
    except(KeyError, IndexError):
        raise RuntimeError("La respuesta no recibe el texto generado en el lugar definido")


def obtener_dato_prueba(pregunta):
    url, body= armar_peticion(pregunta)
    datos = enviar_peticion(url, body)
    
    return extraer_texto(datos)


try:
    print(obtener_dato_prueba("Hola cómo estas"))
except (ValueError, RuntimeError) as error: #Acá manejamos cualquiera de los errores lanzado en la ejecución de las funciones.
    print("No se pudo completar la operación")


# def obtener_dato_de_prueba(pregunta):
#     api_key = os.getenv("GEMINI_API_KEY")
#     modelo = "gemini-flash-latest"
    
#     url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"
#     body = {
#         "contents":[
#             {
#                 "parts": [
#                     {
#                         "text": pregunta
#                     }
#                 ]
#             }
#         ]
#     }
    
#     respuesta = requests.post(url, json = body)
#     datos = respuesta.json()
#     return datos["candidates"][0]["content"]["parts"][0]["text"]

# print(obtener_dato_de_prueba("Confirma en una frase corta que esta conexión funciona"))
