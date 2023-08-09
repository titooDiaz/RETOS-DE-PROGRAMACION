from termcolor import colored
import time

def colorear(numero):
    colores = ['blue', 'magenta']
    for i in range(numero+1):
        if i%2 == 0:
            mensaje = f'{i} es un numero par'
            color = colores[0]
            mensaje_coloreado = colored(mensaje, color)
            print(mensaje_coloreado)
            time.sleep(0.1)
        if i%2 != 0:
            mensaje = f'{i} es un numero impar'
            color = colores[1]
            mensaje_coloreado = colored(mensaje, color)
            print(mensaje_coloreado)
            time.sleep(0.1)

numero = 100
colorear(numero)