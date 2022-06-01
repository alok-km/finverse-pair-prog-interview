class Board:
    def __init__(self):
        self.board = ["-", "-", "-", 
                     "-", "-", "-",
                     "-", "-", "-",]
        self.currentPlayer = "X"
        self.winner = None
        self.gameOver = False

    #printing the board
    def printBoard(self, board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("----------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("----------")
        print(board[6] + " | " + board[7] + " | " + board[8])

    #take player input
    def playerInput(self, board):
        user_input = int(input("Enter a number 1-9: "))
        if (user_input >= 1 and user_input <= 9 and board[user_input - 1] == "-"):
            board[user_input - 1] = self.currentPlayer
        else:
            print("That position on the board has already been filled.")

    #check for win or tie
    def checkHorizontal(self, board):
        if (board[0] == board[1] == board[2] and board[0] != "-"):
            self.winner = board[0]
            return True
        elif (board[3] == board[4] == board[5] and board[3] != "-"):
            self.winner = board[3]
            return True
        elif (board[6] == board[7] == board[8] and board[6] != "-"):
            self.winner = board[6]
            return True

    def checkVertical(self, board): 
        if (board[0] == board[3] == board[6] and board[0] != "-"):
            self.winner = board[0]
            return True
        elif (board[1] == board[4] == board[7] and board[1] != "-"):
            self.winner = board[1]
            return True
        elif (board[2] == board[5] == board[8] and board[2] != "-"):
            self.winner = board[2]
            return True

    def checkDiagonal(self, board):
        if (board[0] == board[4] == board[8] and board[0] != "-"):
            self.winner = board[0]
            return True
        elif (board[2] == board[4] == board[6] and board[2] != "-"):
            self.winner = board[2]
            return True

    def checkTie(self, board):
        if "-" not in board:
            self.printBoard(board)
            print("The game is a tie!")
            self.gameOver = True

    def checkWin(self, board):
        if self.checkDiagonal(board) or self.checkHorizontal(board) or self.checkVertical(board):
            print(f"Game over! The winner is {self.winner}.")
            exit()
            
    #switch the player
    def switchPlayer(self):
        if self.currentPlayer == "X":
            self.currentPlayer = "O"
        else:
            self.currentPlayer = "X"