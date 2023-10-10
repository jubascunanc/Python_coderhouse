
#funcion pyrhon def
def saludar_con_nombre(nombre):
    saludando = print('hola {nombre}! ¿como estas?.format(nombre)')
    return saludando
print('saludando')
saludar_con_nombre("Juan José")


#iterables de datos por nombre
def devuelve_iterables(var1,var2,var3,var4,var5):
    
    return var1, var2, var3, var4, var5

   # print(devuelve_iterables(var1=1,var2=2,var3=3,var4=4,var5=5))
   # print(devuelve_iterables(var2=2,var3=3,var5=5))

print(devuelve_iterables())

#paso por referencia
def agregar_datos(datos):
    print(datos)
    datos.append('otro dato')
    print(datos)

datos = [1,2,3,4,5]
agregar_datos(datos[:])
print(datos)

#funcion recursiva

def cuenta_regrsiva(numero):
    print(numero)
    numero -= 1
    if numero > 0:
      cuenta_regrsiva(numero)
    else:
        print('booom')

    print('fin de la funcion')
        
    print(cuenta_regrsiva)

#funcion magica 
def funcion_magica(valores):

    print(valores)

if len (funcion_magica) == 1:
  print('tienes {valores} en milimetros') == funcion_magica [0]

elif len (funcion_magica)== 2:
  print('tienes {valores} en metros') == funcion_magica [2]

print(funcion_magica)