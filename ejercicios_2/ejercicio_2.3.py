#creando una funcion que muestre la serie fibonacci entre 0 el numero dado

# def fibonacci(num):
#     a,b = 0,1
#     fibonacci_lista = [0]
#     for i in range(num):
#         if b > num: return fibonacci_lista
#         else: 
#             fibonacci_lista.append(b)
#             a,b = b, a+b 
  

# resultado = fibonacci(34)
# print(resultado)

def fibonacci(num):
    
     a,b = 0,1
     fibonacci_lista = []
    
     a = 0 # =1,1,2
     b = 1 # =1,2,3
     contador = a # = 1,1,2,3
     fibonacci_lista.append(contador) # =0,1,1,2,3
     while a < num: 
      a,b = b, a + b # =1,2,3,5    # a= 1,1,2,3 
     return fibonacci_lista 
   
    
      
resultado = fibonacci(34)
print(resultado)

      
       
  
