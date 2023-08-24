# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).


def contar_palabras(cadena):
    
    palabras = cadena.split()
    
    frecuencia = {}
    
    for palabra in palabras:
        
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia
        
            
    
        



cadena = input("Ingresar cadena: ")

resultado = contar_palabras(cadena)

for palabra, frecuencia in resultado.items():
    print(f'{palabra}: {frecuencia}')