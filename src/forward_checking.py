from boards.board import find_empty, is_valid

def forward_checking(board):

    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):

        if is_valid(board, num, (row, col)):

            board[row][col] = num

            if check_forward(board, row, col):
                if forward_checking(board):
                    return True

            board[row][col] = 0

    return False


def check_forward(board, row, col):
    for i in range(9):
        for j in range(9):

            if board[i][j] == 0:

                valid_found = False

                for num in range(1, 10):
                    if is_valid(board, num, (i, j)):
                        valid_found = True
                        break

                if not valid_found:
                    return False

    return True