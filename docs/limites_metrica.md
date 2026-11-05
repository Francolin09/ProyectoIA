# Límites de la métrica de evaluación


## Qué mide

Coincidencia de tokens normalizados (`procesar_texto`) entre
referencia y respuesta, contando repeticiones con `Counter`
para calcular `precision`, `cobertura` y `f1` (`pipeline.py`).


## Modos de falla conocidos

- Respuestas extensas hunden `precision` y `f1` pese a tener
  `cobertura` de 1.0 (ver `resultados_metricas.json`).
- Sinónimos y paráfrasis correctas puntúan bajo al exigir
  coincidencia exacta de tokens tras `limpiar_texto`.
- Fechas o datos erróneos (ej. `1991`) y negaciones cambian
  pocos tokens sin reflejar el error semántico en el puntaje.


## Muestra revisada

3 casos sobre Python en `resultados_metricas.json` (`f1` de
0.030, 0.055 y 0.200), ordenados en `peores_casos` (`[:3]` y
muestra de extremos `peores_casos[:5] + peores_casos[-5:]`).


## Recomendación de uso

Usar `resumir_metricas` (`f1_promedio`) con largo acotado en
`consultar_modelo`, y revisar a mano fechas y explicaciones.
