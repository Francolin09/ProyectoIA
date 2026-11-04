
import re 
from collections import Counter

def limpiar_texto(texto:str)->str:
    #normaliza el texto a minusculas y sin puntuación
    if not isinstance(texto,str):
        tipo = type(texto).__name__
        raise TypeError(f"limpiar_texto espera str no {tipo}")

    texto = texto.lower()
    texto = re.sub(r"[^\w\s]","",texto)
    texto = re.sub(r"\s+"," ",texto).strip()
    return texto

def tokenizar(texto_limpio:str)->list[str]:
    return texto_limpio.split()

def vectorizar(tokens: list[str])-> Counter:
    return Counter(tokens)

if __name__== "__main__":
    texto = "El gato, el perro y el gato corren."
    texto_limpio = limpiar_texto(texto)
    tokens = tokenizar(texto_limpio)
    conteo = vectorizar(tokens)
    print("Texto limpio :", texto_limpio )
    print("tokens: ",tokens)
    print("conteo: ",conteo)