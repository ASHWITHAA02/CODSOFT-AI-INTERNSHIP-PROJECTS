def minimax(board, depth, is_maximizing):

    if board.winner("O"):
        return 1

    if board.winner("X"):
        return -1

    if board.is_full():
        return 0

    if is_maximizing:

        best_score = -100

        for move in board.available_moves():
            board.board[move] = "O"
            score = minimax(board, depth + 1, False)
            board.board[move] = " "

            best_score = max(score, best_score)

        return best_score

    else:

        best_score = 100

        for move in board.available_moves():
            board.board[move] = "X"
            score = minimax(board, depth + 1, True)
            board.board[move] = " "

            best_score = min(score, best_score)

        return best_score


def best_move(board):

    best_score = -100
    move = None

    for i in board.available_moves():
        board.board[i] = "O"
        score = minimax(board, 0, False)
        board.board[i] = " "

        if score > best_score:
            best_score = score
            move = i

    return move