"""
Enunciado:
Implementa un código capaz de leer archivos 'txt' para luego contar cuantas
veces se repite la palabra en el texto. Para ello se crean dos funciones.

La primera llamada 'read_txt_file(path)' que recibe como parámetro
'path' y retorna el texto del archivo que se encuentra en la ruta. El archivo
de texto se debe leer con decodificación "utf-8". Como sigue:
'open(path, "r", encoding="utf-8")'.

La segunda función llamada 'words_counter(text, word)' que recibe como
parametros 'text' y 'word' y retornará el número de palabras encontradas en
el texto.

Se debe leer el archivo que se encuentra en la ruta:
'files/ej6c2_data_engineer.txt'.

Función 'read_txt_file(path)'
    Parámetros:
        path (string): Representa la ruta al archivo.
    Retorna:
        str: Contenido del archivo tipo texto.

Función 'words_counter(text, word)'
    Parámetros:
        text (string): Representa el texto a procesar.
        word (string): Representa la palabra a buscar en el texto.
    Retorna:
        int: Número de ocurrencias de la palabra en el texto.

Ejemplo:
    Entrada:
        text = read_txt_file(path)
        print(words_counter(text, "data"))
    Salida:
        4

Enunciat:

Implementa un codi capaç de llegir arxius 'txt' per després comptar quantes
vegades es repeteix la paraula al text. Per això es creen dues funcions.

La primera anomenada 'read_txt_file(path)' que rep com a paràmetre
'path' i retorna el text del fitxer que es troba a la ruta. El fitxer
de text s'ha de llegir amb descodificació “utf-8”. Com segueix:
'open(path, "r", encoding="utf-8")'.

La segona funció anomenada 'words_counter(text, word)' que rep com
paràmetres 'text' i 'word' i retornarà el nombre de paraules trobades a
el text.

Cal llegir el fitxer que es troba a la ruta:
'files/ej6c2_data_engineer.txt'.

Funció 'read_txt_file(path)'
     Paràmetres:
         path (string): Representa la ruta al fitxer.
     Retorna:
         str: Contingut del fitxer tipus text.

Funció 'words_counter(text, word)'
     Paràmetres:
         text (string): Representa el text a processar.
         word (string): Representa la paraula a cercar al text.
     Retorna:
         int: Nombre d'ocurrències de la paraula al text.

Exemple:
     Entrada:
         text = read_txt_file(path)
         print(words_counter(text, "data"))
     Sortida:
         4

"""


def read_txt_file(path: str) -> str:
   
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def words_counter(text: str, word: str) -> int:
  
  
    text_lower = text.lower()
    word_lower = word.lower()
    
  
    words = text_lower.split()
    return words.count(word_lower)


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# path = "files/ej6c2_data_engineer.txt"
# text = read_txt_file(path)
# print(text[-25:])

# word = "data"
# count = words_counter(text, word)
# print(f"The word '{word}' appears {count} times in the text.")
