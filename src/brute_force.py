from boards.board import find_empty, is_valid

def solve_sudoku_FB(board):
    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):

        board[row][col] = num

        if is_valid(board, num, (row, col)):
            if solve_sudoku_FB(board):
                return True

        board[row][col] = 0

    return False