numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20,21,22]

#creando una funcion lambda para multiplicar por dos/ lambda crea funciones a nominas; es decir que no tienen nombre
multiplicar_por_dos = lambda x : x*2

#creando funcion comun que diga si es par o no
def es_par(numer):
   if (numer%2==1):
       return True
    
#usando filter con una funcion comun 
#/ filter nos crea una lista para mostrarnos si una serie de valores o datos es true o false segun lo requerimois
numeros_pares = filter(es_par,numeros)

#creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))