

def dividir(a,b):
    try:
        valor = a/b
    except:
        print('no se puede dividir por 0')
    else:
        print('la división dio como resultado {valor}')
    finally:
        print('yo te paso por aquí el resultado de tu cuenta')
    
    print('yo te paso el resultado final aquí')

    dividir(5,0)
    dividir(5,1)

  #def dividir(a,b):
    
   # try:
       # print('no se puede dividir por 0')
    #finally:
        #print('termine la operación')