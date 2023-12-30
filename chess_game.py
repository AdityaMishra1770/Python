import chess

def print_board(board):
    print(board)

def get_move():
    uci_move = input("Enter your move: ")
    return uci_move

def play_game():
    board = chess.Board()
    while not board.is_checkmate() and not board.is_stalemate() and not board.is_insufficient_material() and not board.is_seventyfive_moves() and not board.is_fivefold_repetition() and not board.is_variant_draw():
        print_board(board)
        uci_move = get_move()
        if chess.Move.from_uci(uci_move) in board.legal_moves:
            board.push(chess.Move.from_uci(uci_move))
        else:
            print("Illegal move. Try again.")
    print_board(board)
    if board.is_checkmate():
        print("Checkmate!")
    elif board.is_stalemate():
        print("Stalemate!")
    elif board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition() or board.is_variant_draw():
        print("Draw!")

play_game()
