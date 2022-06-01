import board

board_object = board.Board()

def main():
    while board_object.gameOver != True:
        board_object.printBoard(board_object.board)
        board_object.playerInput(board_object.board)
        board_object.checkWin(board_object.board)
        board_object.checkTie(board_object.board)
        board_object.switchPlayer()

main()