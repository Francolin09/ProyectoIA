from pipeline_limpieza import procesar_texto
from pipeline_limpieza import *
from cliente import consultar_modelo

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


# referencia = "El cielo es azul."
# respuesta = "el cielo es azul"

# tokens_referencia = procesar_texto(referencia)
# tokens_respuesta = procesar_texto(respuesta)

# comunes = set(tokens_referencia) & set(tokens_respuesta)
# print(comunes)

# if tokens_referencia:
#     proporcion = len(comunes) / len(set(tokens_referencia))
#     #2/4 = 0.5 = 50%
# else:
#     proporcion = 0.0

# print(f"Coincidencia: {proporcion:.0%}")

###################################################

consulta = "Qué es python"

referencia = "python es un lenguaje de programación interpretado"

respuesta = consultar_modelo(consulta)

texto_crudo_ref = referencia.split()
texto_crudo_resp = respuesta.split()

comunes_crudo = set(texto_crudo_ref) & set(texto_crudo_resp)

proporcion_crudos = len(comunes_crudo)/ len(set(texto_crudo_ref))

tokens_ref = procesar_texto(referencia)
tokens_resp = procesar_texto(respuesta)

comunes = set(tokens_ref) & set(tokens_resp)
proporcion_procesados = len(comunes) / len(set(tokens_ref))

print(f"[Caso 1] Coincidencia texto crudo {proporcion_crudos:.1%}")
print(f"[Caso 2] Coincidencia texto procesado {proporcion_procesados:.1%}")
#Este funciona pero omite cuando una palabra se repite y eso puede generar problemas entendiendo el contexto

def contar_coincidencias(tokens_referencia:list[str], tokens_respuesta:list[str]) -> int:
    conteo_referencia = Counter(tokens_referencia)
    conteo_respuesta = Counter(tokens_respuesta)
    interseccion = conteo_referencia & conteo_respuesta

    return sum(interseccion.values())
print(tokens_resp)
print(tokens_ref)    
print(contar_coincidencias(tokens_ref,tokens_resp))

def calcular_precision_cobertura_f1(tokens_referencia: list[str],tokens_respuesta: list[str],) -> dict[str, float]:
    """Calcula precisión, cobertura y F1 de dos listas de tokens."""
    coincidencias = contar_coincidencias(tokens_referencia, tokens_respuesta)

    if not tokens_respuesta or not tokens_referencia:
        return {"precision": 0.0, "cobertura": 0.0, "f1": 0.0}

    precision = coincidencias / len(tokens_respuesta)
    cobertura = coincidencias / len(tokens_referencia)

    if precision + cobertura == 0:
        f1 = 0.0
    else:
        f1 = 2 * precision * cobertura / (precision + cobertura)

    resultado = {
        "precision": precision,
        "cobertura": cobertura,
        "f1": f1,
    }

    return resultado