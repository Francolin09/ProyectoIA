import cliente
from cliente import con_reintento, consultar_modelo
from unittest.mock import patch, Mock

import pytest

from src.consumir_gemini import enviar_peticion


def test_enviar_peticion_credencial_invalida():
    respuesta_falsa = Mock(status_code=401)
    #patch remplaza la funcion requests.post por nuestra respuesta falsa
    with patch("src.consumir_gemini.requests.post", return_value=respuesta_falsa):
        with pytest.raises(ValueError):
            enviar_peticion("https://ejemploinvalid",{"pregunta": "test"})
            #Entonces acá al final se ejecuta nuestra respuesta falsa 

def test_enviar_peticion_limite_de_uso():
    respuesta_falsa = Mock(status_code=429)

    with patch("src.consumir_gemini.requests.post", return_value = respuesta_falsa):
        with pytest.raises(TimeoutError):
            enviar_peticion("https://ejemplito",{"pregunta": "test"})

def test_enviar_peticion_exito():
    respuesta_falsa = Mock(status_code = 200)
    respuesta_falsa.json.return_value = {"texto":"respuesta simulada"}

    with patch("src.consumir_gemini.requests.post", return_value = respuesta_falsa):
        resultado = enviar_peticion("asda",{"pregunta": "test"})

    assert resultado == {"texto":"respuesta simulada"}    

def test_con_reintento_agota_intentos():
    def siempre_falla():
        raise TimeoutError("simulado")

    with patch("cliente.time.sleep"):
        with pytest.raises(TimeoutError):
            con_reintento(siempre_falla, intentos=3)    

def test_con_reintento_no_reintenta_otra_excepcion():
    funcion_falsa = Mock(side_effect=ValueError("credencial invalida"))
    with patch("cliente.time.sleep"):
        with pytest.raises(ValueError):
            con_reintento(funcion_falsa, intentos=3)
    assert funcion_falsa.call_count == 1

def test_consultar_modelo_convierte_error():
    error_simulado = TimeoutError("simulado")

    with patch("cliente.con_reintento", side_effect=error_simulado):
        with pytest.raises(RuntimeError):
            consultar_modelo("pregunta de prueba")

def test_registrar_costo_acumula():
    cliente.costo_total_sesion = 0
    respuesta_falsa = {"usageMetadata": {"totalTokenCount": 1000}}
    costo = cliente.registrar_costo(respuesta_falsa)

    assert costo == cliente.COSTO_POR_1000_TOKENS
    assert cliente.costo_total_sesion == cliente.COSTO_POR_1000_TOKENS