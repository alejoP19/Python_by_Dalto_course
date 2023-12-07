
#creando una lista (¡Sí! se puede modificar)
lista = ["Mario Alejandro", "Soy Programador",True, 1.73]

#creando una tupla (¡No! se puede modificar)
tupla = ("Mario Alejandro", "Soy Programador",True, 1.73)

#esto es valido
# lista[1] ="Soy musico" 
print(lista[0])

#esto es No es valido
# tupla[1] ="Soy musico" 
# print(tupla[1])

#creando una conjunto set (¡No! se usan () ni [] se usan {}) 
# el orden de los datos puede cambiar
#como en las tuplas no podemos cambiar el dato; pero si redefinir el contenido del conjunto

#creando un conjunto (set) (no se accede a elementos por ìndice ejemplo: #print(conjunto[2],
# no almacena datos duplicados)
conjunto = {"Mario Alejandro", "Soy Programador",True, 1.73}

#conjunto = {"Pedro sarigueyo", "campesino",True, 1.50}

#creando un diccionario (dict)
#La estructur es key/value y se separan por comas
diccionario ={
    'nombre' : "Mario Echeverry",
    'profesión' : "programador y musico",
    'está feliz?' : True,
    'altura' : 1.75,
    'dato_duplicado' : "programador y musico"
       
}
print(diccionario['altura'])