# Ejemplo de iterador

#Crear una lista
my_list = [1,2,3,4,5]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Iterar en cadenas
# Creando la cadena

text = "Hola Mundo"
#Creando el iterador

iter_text = iter(text)

#Iterar en la cadena
for char in iter_text:
    print(char)

 # Crear un iterador para los numeros impares
 
 #Limite
limit = 10

#Crear iterador
# inicia desde uno sumandolo e ioterando cada 2 numeros, por lo que son impares
odd_itter = iter(range(1,limit+1,2))

# Usar el iterador

for num in odd_itter:
    print(num)
    
# yield para que devuelva un valor
 
def my_generator():
     yield 1
     yield 2
     yield 3

for value in my_generator():
    print(value)     
    
#Fibonacci
# 0 1 1 2 3 5 8 13 21...

def fibonacci(limit):
    a, b = 0,1
    while  a< limit:
        yield a
        a, b = b, a+b

for num in fibonacci(10):
    print(num)    
        
        