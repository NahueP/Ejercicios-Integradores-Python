# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.


#VERSION ITERATIVA
def get_int():
    flag = True
    
    while flag:
        try:
            valor = int(input("Ingrese un valor: "))
            flag = False
            return valor
        except ValueError:
            print("El valor ingresado no es entero")
     

#VERSION RECURSIVA
def get_int_rec():
    try:
        valor = int(input("Ingrese un valor: "))
        return valor
    except ValueError:
        print("El valor ingresado no es entero")
        return get_int_rec()
    
##########################################################            
            
valor = get_int()
print("Ha ingresado el valor entero: ", valor)
            
            
