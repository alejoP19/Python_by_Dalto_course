#Promedio de duraciòn
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duraciòn

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
# diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max  / 10
diferencia_con_max = round(100 - dalto_curso / otros_cursos_max *100,1)

diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#Calculando el porcentaje de tiempo vacìo removido
# tiempo_vacio_promedio =  100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_promedio= round(100 - otros_cursos_promedio / crudo_promedio *100,1)
# tiempo_vacio_dalto =  100 - dalto_curso * 1000 // crudo_dalto / 10
tiempo_vacio_dalto= round(100 - dalto_curso / crudo_dalto *100,1)


#Mostrando las diferencias de duraciòn (ejercicio A)

print("----------------")
print("El curso de dalto dura:")
print(f' - un {diferencia_con_min}% menos que el màs rapido')
print(f' - un {diferencia_con_max}% menos que el màs lento')
print(f' - un {diferencia_con_promedio}% menos que el promedio')
print("----------------")

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso eliminò el {tiempo_vacio_dalto}% de tiempo vacio')
print("----------------")

#Mostrando diferencias si los cursos duraran 10 horas (ejercicio C)
print(f'Ver 10 horas de este curso equivale a ver { round(otros_cursos_promedio / dalto_curso * 10,1)} horas de otros cursos')
# tiempo_vacio_dalto= round(100 - dalto_curso / crudo_dalto *100,1)
print(f'Ver 10 horas de otros cursos equivale a ver {round(dalto_curso / otros_cursos_promedio * 10,1)} horas de este curso')
print("----------------")
