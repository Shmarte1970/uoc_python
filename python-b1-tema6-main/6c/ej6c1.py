"""
Enunciado:
Utilizando la librería NLTK, implementa una función 'sentiment_analysis(text)'
que recibe como parámetro 'text' que es una cadena de strings, la misma que
debe ser analizada para saber si esa frase representa una emoción negativa o
positiva.

Se debe utilizar 'SentimentIntensityAnalyzer' que es importada desde 
'nltk.sentiment', de esta manera obtendremos una puntuación en base al número
de palabras que se esten asociando a algo positivo o negativo dentro de la frase
analizada.

Utilizaremos el módulo nltk.sentiment.vader para analizar el sentimiento de un texto.
Te recmendamos que revises la documentación:
https://www.nltk.org/api/nltk.sentiment.vader.html

En concreto, revisa la función polarity_scores(text) 

Si la puntuación es mayor de 0.05 se retorna un resultado positivo, si es menor
a -0.05 se retorna un resultado negativo y si se encuentra entre los valores
-0.05 y 0.05 inclusives, se retorna un resultado neutro.

Parámetro:
text: Cadena de strings.

Ejemplo:
    Entrada:
        "I love going to the beach on a sunny day, but I hate getting 
        sunburned."

    Salida:
        "Negative"

Enunciat:
Utilitzant la llibreria NLTK, implementa una funció 'sentiment_analysis(text)'
que rep com a paràmetre 'text' que és una cadena de strings, la mateixa que
ha de ser analitzada per saber si aquesta frase representa una emoció negativa o
positiva.

S'ha d'utilitzar 'SentimentIntensityAnalyzer' que és importada des de
'nltk.sentiment', d'aquesta manera obtindrem una puntuació sobre la base del número
de paraules que s'estiguin associant a alguna cosa positiva o negativa dins la frase
analitzada.

Utilitzarem el mòdul nltk.sentiment.vader per a analitzar el sentiment d'un text.
Et recmendamos que revisis la documentació:
https://www.nltk.org/api/nltk.sentiment.vader.html

En concret, revisa la funció polarity_scores(text)

Si la puntuació és més gran de 0.05 es retorna un resultat positiu, si és menor
a -0.05 es retorna un resultat negatiu i si es troba entre els valors
-0.05 i 0.05 inclusives, es retorna un resultat neutre.

Paràmetre:
text: Cadena de strings.

Exemple:
     Entrada:
         "I love going to the beach on a sunny day, but I hate getting
         sunburned."

     Sortida:
         "Negative"

"""
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def sentiment_analysis(text):
    
    sia = SentimentIntensityAnalyzer()
    
    
    scores = sia.polarity_scores(text)
    compound_score = scores['compound']
    
    
    if compound_score > 0.05:
        return "Positive"
    elif compound_score < -0.05:
        return "Negative"
    else:
        return "Neutral"


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# text = "This product is okay."
# print(sentiment_analysis(text))
