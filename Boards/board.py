#Función para imprimir el tablero de Sudoku
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


#Función para encontrar un espacio vacío en el tablero de Sudoku
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None



#Función para verificar si un número es válido en una posición dada en el tablero de Sudoku
def is_valid(board, num, pos):
    row, col = pos

    #Revisa fila
    for j in range(len(board[0])):
        if board[row][j] == num and col != j:
            return False

    # revisar columna
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    # revisar subcuadro 3x3
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True