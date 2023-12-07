diccionario = {
    "nombre" : 'lucas',
    "apellido" : 'dalto',
    "subs" : 1000000
}

#nos devuelve un objeto dict_item (devuelve las claves) / también nos sirve para iterar
claves = diccionario.keys()
# print(claves)

#obteniendo un elemento con get() (si no encuentra nada el programa continùa)
#a diferencia de otro metodos da error y se frena el programa yua que no encuentra el dato
valor_de_kasdks = diccionario.get("kasdks")
print(valor_de_kasdks)
print("Eso perrito! El programa")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)