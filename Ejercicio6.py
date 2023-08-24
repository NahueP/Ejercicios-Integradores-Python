# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
        
    #GETTERS
    def get_nombre(self):
        return self.nombre
    
    def  get_edad(self):
        return self.edad
        
    def get_dni(self):
        return self.dni
    
    #SETTERS
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_edad(self,edad):
        self.edad = edad
    
    def set_dni(self,dni):
        self.dni = dni
        
    
    def Es_mayor_de_edad(self):
        return self.edad >= 18 if self.edad is not None else False
        
        
    def mostrar(self):
        print("Nombre", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
        
        
        
persona = Persona()

persona.set_nombre("nahuel")
persona.set_edad(25)
persona.set_dni("40123321")


persona.mostrar()

if persona.Es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("Es menor de edad")