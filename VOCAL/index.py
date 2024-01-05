vocales = 'aeiouAEIOU'
def vocal(vol):
    if vol in vocales:
        return True
    else:
        return False

if vocal('A'):
    print('valido')
else:
    print('no valido')