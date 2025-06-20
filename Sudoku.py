import time

# Función para imprimir el tablero
def print_sudoku(sudoku):
    for fila in sudoku:
        print(" ".join(str(num) if num != 0 else "." for num in fila))

# Función para validar si un número se puede colocar en cierta posición
def valido(sudoku, n, i, j):
    for x in range(9):
        if sudoku[i][x] == n or sudoku[x][j] == n:
            return False
    fila_ini = (i // 3) * 3
    col_ini = (j // 3) * 3
    for x in range(fila_ini, fila_ini + 3):
        for y in range(col_ini, col_ini + 3):
            if sudoku[x][y] == n:
                return False
    if i == j:
        for k in range(9):
            if sudoku[k][k] == n:
                return False
    if i + j == 8:
        for k in range(9):
            if sudoku[k][8 - k] == n:
                return False
    return True

# Función recursiva para resolver el Sudoku
operaciones = 0
def resolver(sudoku):
    global operaciones
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for n in range(1, 10):
                    operaciones += 1
                    if valido(sudoku, n, i, j):
                        sudoku[i][j] = n
                        if resolver(sudoku):
                            return True
                        sudoku[i][j] = 0
                return False
    return True

# Tablero inicial
sudoku = [
    [0, 9, 0, 8, 0, 7, 0, 4, 0],
    [0, 1, 0, 4, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 9, 0, 3, 2, 0, 0, 3],
    [0, 5, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 7, 1],
    [0, 0, 6, 0, 7, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Ejecución del programa
inicio = time.time()
resolver(sudoku)
fin = time.time()
print("Sudoku resuelto:")
print_sudoku(sudoku)
print(f"\nTiempo de ejecución: {fin - inicio:.4f} segundos")
print(f"Operaciones realizadas: {operaciones}")




