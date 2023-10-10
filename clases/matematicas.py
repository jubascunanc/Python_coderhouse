
valores = [3,6,9,12,24]

def suma_elementos(*valores):

    suma = sum(valores)

if suma_elementos > 24:
    print("la operación es menor a 24")
elif suma_elementos < 24:
    print("la operación es mayor a 24")

print(suma_elementos)



