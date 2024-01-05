numeros=[1,2,3,4]

def sum(x):
    suma=0
    for i in x:
        suma += i
    return suma

def mul(x):
    multiplicar = 1
    for i in x:
        multiplicar *= i
    return multiplicar

print(sum(numeros)) # deberia dar 10
print(mul(numeros)) # deberia dar 24