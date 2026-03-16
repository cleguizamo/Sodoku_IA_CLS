from boards.board import find_empty, is_valid

def solve_backtracking(board):
    empty = find_empty(board)

    if not empty:
        return True
    
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_backtracking(board):
                return True
            
            board[row][col] = 0

    return False