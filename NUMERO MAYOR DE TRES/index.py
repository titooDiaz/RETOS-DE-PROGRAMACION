def num_mayor_3(num1,num2,num3):
    if num1 > num2 and num1>num3:
        print(f'{num1} es el mayor')
    elif num2 > num1 and num2 > num3:
        print(f'{num2} es el mayor')
    else:
        print(f'{num3} es el mayor')
# Comprobar si un número es mayor que 3.
num_mayor_3(3,9,10)