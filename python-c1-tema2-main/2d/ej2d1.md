En este ejercicio  creo que esta mal planteado 
No se puede utilizar jsonify porque los endpoints deben devolver texto plano.
La función jsonify siempre genera respuestas con Content-Type: application/json, mientras que el test comprueba que la respuesta sea text/plain.

Lo he cambiado por request.