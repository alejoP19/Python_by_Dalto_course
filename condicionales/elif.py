ingreso_mensual = 72000
gasto_mensual = 80000

#if anidados  y else_if  (elif)
if ingreso_mensual > 10000:
    if ingreso_mensual  -  gasto_mensual < 0:
        print ("Estas en deficit")
    elif  ingreso_mensual  -  gasto_mensual > 3000: 
     print ("estás bien")  
    else: 
        print ("No estás gastando moderadamente")
        
elif  ingreso_mensual > 1000:
       print ("Estás bien de lucas en latinoamerica")
       
elif  ingreso_mensual > 500:
   print ("Estás bien de lucas en argentina")
   
elif  ingreso_mensual > 200:
   print ("Estás bien de lucas en colombia")

else:
       print ("Eres un perdedor")       