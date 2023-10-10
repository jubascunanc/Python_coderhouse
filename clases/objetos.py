
class Auto:

    def _init_(self, marca, modelo,color ):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def descripcion(self):
        print('este es un auto')

    def tocar_bocina(self):
        print('piiiiiii')

    def asignar_color(self, color):
        self.color = color

    def modificar_color(self, color):
        self.color = color

    def mostrar_color(self):
        print(self.color)
        
        
auto1= Auto('Ford', 'K', 'rojo')
auto2= Auto('Mercedez','L', 'Negro')
    
print(auto1)
print(auto2)

auto1.tocar_bocina()
auto2.tocar_bocina()

auto1.descripcion()
auto2.descripcion()

auto1.mostrar_color()