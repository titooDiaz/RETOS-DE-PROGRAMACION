def invertir_cadena(x):
    resultado = ''
    for i in x:
        resultado = i + resultado
    return resultado

print(invertir_cadena("SATSE OMOC ALOH"))