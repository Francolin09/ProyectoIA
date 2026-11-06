from dotenv import load_dotenv
import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate #Plantilla que incluye rol del sistema e instruccion 
load_dotenv()

modelo= ChatGoogleGenerativeAI(model = "gemini-3.6-flash")
#respuesta = modelo.invoke("Qué es un token") 
#print(respuesta.content)

plantilla = PromptTemplate.from_template("Explica el concepto de {tema} en un parrado, para alguien que recién comienza en {area}")

# prompt = plantilla.invoke(
#     {
#     "tema":"tokenización",
#     "area": "procesamiento de texto"
#     }
#     )

# print(prompt.text)

cadena_simple = plantilla | modelo | StrOutputParser() #Une ambas variables

respuesta =  cadena_simple.invoke(
    {"tema":"embeddings", "area":"Busqueda semántica"}
)

print(respuesta)

plantilla_control = ChatPromptTemplate.from_messages([
    {"system", "Eres un experto en {area} y vas a responder siempre con un texto simple para el usuario"},
    {"human","Explica el concepto de {tema} en un párrafo, para alguien que recien comienza en {area}"}
])
