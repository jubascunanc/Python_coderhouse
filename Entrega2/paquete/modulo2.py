
from modulo1 import Cliente

print(Cliente)

print("Hola cliente Juanjose")

#Items tienda comercial
print("Elige los articulos que quieres comprar:")

class Tienda:
   
    pass
   
    def __init__(self,articulo,valor,categoria):
        self.articulo = articulo
        self.valor = valor
        self.categoria = categoria
    def __str__(self) -> str:
        return f"Articulo:{self.articulo} Valor: {self.valor} Categoria: {self.categoria}"
        
Compra1 =   Tienda("chocolate", "1.500", "dulces")
Compra2 =   Tienda("coca-cola", "500", "bebida")
Compra3 =   Tienda("hamburguesa", "3000","comida")
Compra4 =   Tienda("Hot dog","1000","comida")

def suma_total(Tienda):

    total = 0
    print(Tienda(Compra1+ Compra2 + Compra3 + Compra4))

    print(suma_total)