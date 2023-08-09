def romano_a_arabigo(romano):
    numeros_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    arabigo = 0
    numero_ant = 0

    for o in romano:
        if numeros_romanos[o] > numero_ant:
            arabigo += numeros_romanos[o] - 2 * numero_ant
        else:
            arabigo += numeros_romanos[o]
        numero_ant = numeros_romanos[o]

    return arabigo

# Ejemplo de uso
numero_romano = "XX"
numero_arabigo = romano_a_arabigo(numero_romano)
print(numero_arabigo)