#creando una funciòn simple
#def saludar():
#   print("Hola lucas, mi maestro ¿Como andas?")
    
#ejecutando la funcion simple
#saludar()

#crear una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = 'amor'
    print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")
    
    
saludar("Camila","MuJER")
saludar("Dalto","hombre")
saludar("Fran","no binario")

#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)  # El número que le damos en este caso de tres digitos(981) cuenta como string.
    num = int(num_entero[1]) #  toma el numero de la posicion [1] para hacer el resto de las operaciones; es decir el [8]
    c1 = num - 2 # le resta 2 al 8 = 6
    c2 = num     # coloca el numero 8 ya que no se le pide hacer nada con el
    c3 = num - 5 #le resta 5 al 8 = 3
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}" # con el resultado de cada caracter (c1,c2,c3) busca en chars 
    # la posición de la letra en este caso c1= g, c2=i, c3=16 y finalmente multiplica el numero dado 8 * 2 = 16.
    return contraseña,num
    
#desempaquetando la funciòn
password,primer_numero = crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El nùmero utilizado para crearla fue: {primer_numero}")



