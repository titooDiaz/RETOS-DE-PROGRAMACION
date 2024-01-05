def superposicion(lista1, lista2):
    """Esta función devuelve True si hay almenos una igual"""
    for o in lista1:
        for i in lista2:
            if o == i:
                return True
    return False
lista1 = [8,2,3]
lista2 = [4,4,5]
print(superposicion(lista1, lista2))