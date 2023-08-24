# 1. Escribir una función que calcule el máximo común divisor entre dos números.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))



def MaximoComunDivisor(num1, num2):
    #Primero MCD de num1
    mcd = 1
    
    if num1 % num2 == 0:
        return num2 
    
    for i in range(int(num2/2),0,-1):
        if(num1 % i == 0 and num2 % i == 0):
            mcd = i
            break
    
    return mcd

print(MaximoComunDivisor(numero1,numero2))