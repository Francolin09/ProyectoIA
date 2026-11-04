from pipeline_limpieza import procesar_texto
from pipeline_limpieza import *

# referencia = "El cielo es azul."
# respuesta = "el cielo es azul"

# tokens_referencia = referencia.split()
# tokens_respuesta = respuesta.split()

# comunes = set(tokens_referencia) & set(tokens_respuesta)
# print(comunes)

# if tokens_referencia:
#     proporcion = len(comunes) / len(set(tokens_referencia))
#     #2/4 = 0.5 = 50%
# else:
#     proporcion = 0.0

# print(f"Coincidencia: {proporcion:.0%}")        

############################################


referencia = "El cielo es azul."
respuesta = "el cielo es azul"

tokens_referencia = procesar_texto(referencia)
tokens_respuesta = procesar_texto(respuesta)

comunes = set(tokens_referencia) & set(tokens_respuesta)
print(comunes)

if tokens_referencia:
    proporcion = len(comunes) / len(set(tokens_referencia))
    #2/4 = 0.5 = 50%
else:
    proporcion = 0.0

print(f"Coincidencia: {proporcion:.0%}")