# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números


numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))



def MinimoComunMultiplo(num1, num2):
    mcm = max(num1,num2)
    
    while True:
        if (mcm % num1 == 0) and (mcm % num2 == 0):
            return mcm
        
        mcm += 1
   

print(MinimoComunMultiplo(numero1,numero2))