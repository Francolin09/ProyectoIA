from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI #Modelo
from langchain_core.prompts import PromptTemplate #Plantilla - prompt dinámico
from langchain_core.output_parsers import StrOutputParser #Parsea la respuesta y transforma en solo texto útil
from langchain_core.prompts import ChatPromptTemplate #Plantilla que incluye rol de sistema e instruccion

load_dotenv()

modelo = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

plantilla_extraccion = PromptTemplate.from_template("Lee el siguiente texto y devuelve solo sus 3 puntos clave, uno por uno, sin desarrollarlos :\n\n {texto}")

paso_extraccion = plantilla_extraccion | modelo | StrOutputParser()

texto_prueba = (
    "Los modelos de lenguaje grandes generan texto "

    "prediciendo un token a la vez, basándose en el "

    "texto que ya generaron antes. Cada token puede "

    "ser una palabra completa, parte de una palabra, "

    "o un signo de puntuación. Antes de que el modelo "

    "genere una respuesta, el texto de entrada se "

    "divide en tokens, un proceso llamado tokenización."
    )
#Paso 1
puntos = paso_extraccion.invoke({"texto": texto_prueba})

print(puntos)

#Paso 2 

plantilla_simplificacion = PromptTemplate.from_template("Reescribe estos puntos en lenguaje simple, sin jerga técnica para alguien sin conocimientos previos: \n\n {puntos}")

paso_simplificacion = plantilla_simplificacion | modelo | StrOutputParser()

simple = paso_simplificacion.invoke(
    {"puntos", puntos}
)

print(simple) #El segundo paso utiliza la respuesta del primer paso

#Paso 3
plantilla_formato = PromptTemplate.from_template("Convierte este texto en una lista de viñetas markdown de máximo 3 lineas, sin introduccion: \n\n{texto_simple}")

paso_formato = plantilla_formato | modelo | StrOutputParser()

formateado = paso_formato.invoke(
    {"texto_simple":simple}
)

print(formateado)
