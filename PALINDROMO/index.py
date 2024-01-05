def invertir_cadena(x):
    resultado = ''
    for i in x:
        resultado = i + resultado
    if resultado == x:
        return True
    return False

print(invertir_cadena("ana"))