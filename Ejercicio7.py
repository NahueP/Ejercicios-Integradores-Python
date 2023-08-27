# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.

from Ejercicio6 import Persona

class Cuenta:
    
    def __init__(self, titular, cantidad = 0.0):
        self.titular = titular
        self.cantidad = cantidad
        
    
    #GETTERS
    def get_titular(self):
        return self.titular
    
    def get_cantidad(self):
        return self.cantidad
        
    #SETTERS
    def set_titular(self,titular):
        self.titular = titular
        
    def set_cantidad(self,cantidad):
        self.cantidad = cantidad
        
    
    #METODOS
    
    def mostrar(self):
        print("Titular: ", self.titular.nombre)
        print("Edad: ", self.titular.edad)
        print("DNI: ", self.titular.dni)
        print("Cantidad: ", self.cantidad)
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad ingresada debe ser mayor a cero")
            
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
        else:
            print("La cantidad ingresada debe ser mayor a cero")
            
            

cuenta = Cuenta(Persona('Nahuel', 25, 40123321), 50000)

cuenta.mostrar()


print("Ignresando dinero...")
cuenta.ingresar(15000)
cuenta.mostrar()

print("Retirando dinero...")
cuenta.retirar(30000)
cuenta.mostrar()

