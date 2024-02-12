def fugg(p1):
    return len(p1)

lista = [1, 2, 3]
#print(fugg(lista))

def fugg1(n):
    print(n)
    if n > 1:
       fugg1(n - 1) 
fugg1(10)

# 0 1 1 2 3 5 8 13 

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
    
print(fibonacci(8))

# 4! = 4 * 3 * 2 * 1 = 24
# 4! = 4 * 3!
# 4! = 4 * 3 * 2!
# 4! = 4 * 3 * 2 * 1!
# 1! = 1
def faktorialis(n):
    if n == 1:
        return 1
    else:
        return n * faktorialis(n - 1)
    

print(faktorialis(4)) # 24

#a**b = a * a**(b-1)
#a**0 = 1
#0**b = 0
#a**1 = a
def hatvany(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * hatvany(a, b - 1)
    
print(hatvany(2, 3))