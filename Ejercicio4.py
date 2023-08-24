# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.



def contar_palabras(cadena):
    
    palabras = cadena.split()
    
    frecuencia = {}
    
    for palabra in palabras:
        
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia
        
            
    

def palabras_repetidas(diccionario):
    
    palabra = max(diccionario, key=diccionario.get)

    frecuencia = diccionario[palabra]
    
    return palabra, frecuencia



cadena = "pablito clavo un clavito que clavito clavo pablito"
frecuencia = contar_palabras(cadena)
palabraRepetida, frecuenciaRepetida = palabras_repetidas(frecuencia)

print(f'Palabra más repetida: "{palabraRepetida}" con una frecuencia de {frecuenciaRepetida} veces.')