
#de esta manera podemos contar los string en una lista

#metodo find
cadena1 = 'soy un parrafo';
print(cadena1.find('a')) #el elemento se cuenta 2 veces
print(cadena1.find('o', 1))
print(cadena1.find('oy'))
print(cadena1.count('soy'))
print(cadena1.rfind('parrafo'))

#metodo split
cadena2 = 'este es un string';
cadena2_split = cadena2.split()
print(cadena2)
print(cadena2_split)

#metodo strip
password = input('ingrese un password:')

print(password.strip())

#metodo join

texto = 'este es mi ejercicio con metodos'

texto_split = texto.split()
print(texto.join())

diccionario = ['auto', 'moto', 'barco','camion']

print(diccionario.append('casa'))