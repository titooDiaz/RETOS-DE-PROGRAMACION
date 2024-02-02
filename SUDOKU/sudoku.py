def imprimir_sudoku(sudoku):
    for fila in sudoku:
        print(" ".join(fila))

def encontrar_celda_vacia(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == '-':
                return i, j
    return None

def es_numero_valido(sudoku, fila, columna, num):
    # Verificar en la fila
    if num in sudoku[fila]:
        return False

    # Verificar en la columna
    if num in [sudoku[i][columna] for i in range(9)]:
        return False

    # Verificar en el cuadrante 3x3
    cuadrante_fila, cuadrante_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(cuadrante_fila, cuadrante_fila + 3):
        for j in range(cuadrante_columna, cuadrante_columna + 3):
            if sudoku[i][j] == num:
                return False

    return True

def resolver_sudoku(sudoku):
    celda_vacia = encontrar_celda_vacia(sudoku)
    print(celda_vacia)

    if not celda_vacia:
        # El sudoku está resuelto
        return True

    fila, columna = celda_vacia

    for num in map(str, range(1, 10)):
        if es_numero_valido(sudoku, fila, columna, num):
            sudoku[fila][columna] = num

            if resolver_sudoku(sudoku):
                return True

            sudoku[fila][columna] = '-'

    # No hay solución con el número actual, retroceder
    return False

# Sudoku dado
sudoku = [
    ['1','-','-','9','7','-','3','5','6'],
    ['9','3','6','5','8','1','-','-','4'],
    ['5','-','-','3','-','-','8','9','1'],
    ['-','-','3','-','-','7','-','-','9'],
    ['6','-','-','-','3','-','-','-','7'],
    ['2','-','-','-','-','-','5','1','3'],
    ['8','-','-','-','4','-','9','3','2'],
    ['7','-','4','-','-','3','-','-','8'],
    ['3','-','-','-','-','8','-','-','5'],
]

print("Sudoku Original:")
imprimir_sudoku(sudoku)

if resolver_sudoku(sudoku):
    print("\nSudoku Resuelto:")
    imprimir_sudoku(sudoku)
else:
    print("\nNo hay solución para el Sudoku dado.")
