def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_5 = print(factorial(5))

def fibonacci(i):
    if i == 0:
        return(0)
    elif i ==1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)
    
number = 3
print(fibonacci(number))    
