#Saludo
print("HOla vienvenido al registro de nuestra página")

#Input cliente
input("Ingrese su nombre aquí:")
def Usuario(nombre):
    nombre = "Juanjose";
print(Usuario)

#clase cliente
class Cliente:
    pass

    def __init__(self, nombre, apellido, direccion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Direccion: {self.direccion}")
        print(f"Telefono: {self.telefono}")

#registro

Cliente1 = Cliente ("Juanjose","Bascuñan","camino aguada 10371","994939198")

Cliente1.mostrar_informacion()

