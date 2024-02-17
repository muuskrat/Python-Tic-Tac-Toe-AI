import random

class TTT_cs170_judge:
    def __init__(self):
        self.board = []
        
    def create_board(self, n):
        for i in range(n):
            row = []
            for j in range(n):
                row.append('-')
            self.board.append(row)
            
    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()
            
    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        
        # Check columns
        for col in range(len(self.board)):
            if all([self.board[row][col] == player for row in range(len(self.board))]):
                return True
        
        # Check diagonals
        if all([self.board[i][i] == player for i in range(len(self.board))]):
            return True
        if all([self.board[i][len(self.board) - i - 1] == player for i in range(len(self.board))]):
            return True
        
        return False
    
    def is_board_full(self):
        return all([cell in ['X', 'O'] for row in self.board for cell in row])
    

class Player_1:
    def __init__(self, judge):
        self.board = judge.board
    
    def my_play(self):
        while True:
            row, col = map(int, input("Enter the row and column numbers separated by space: ").split())
            
            if 1 <= row <= len(self.board) and 1 <= col <= len(self.board[0]):
                self.board[row-1][col-1] = 'X'
                break
            else:
                print("Wrong coordination!")





class Player_2:
    def __init__(self, judge):
        self.judge = judge
        self.board = judge.board
    
    def my_play(self):
        if not self.judge.is_board_full():
            self.minimax(self.board, 'O', 'X')
            row, col = self.choice
            self.board[row][col] = 'O'

    def minimax(self, board, maxp, minp):
        #base condition for recursive method
        if self.judge.is_winner('O'):
            return 1
        elif self.judge.is_winner('X'):
            return -1
        elif self.judge.is_board_full():
            return 0

        #empty array of scores and moves that will be populated later
        scores = [] 
        moves = [] 

        #looping through 2D array to find legal spots
        # '-' means the spot in the array is empty 
        for i in range(len(board)):
            for j in range(len(board[i])):

                #main recursive loop 
                #if an empty spot is found recursivly call minmax
                if board[i][j] == '-':
                    board[i][j] = maxp
                    #find out what the end score is by switching players and storing it
                    score = self.minimax(board, minp, maxp)
                    board[i][j] = '-'
                    #storing score and location of move
                    scores.append(score)
                    moves.append((i, j))

        #finally decide best move
        #if the AI is first then it wants to choose the max score to win
        #else the AI will choose the lowest score as if it was trying to lose as the player
        if maxp == 'O':
            max_score_index = scores.index(max(scores))
            self.choice = moves[max_score_index]
            return max(scores)
        else:
            min_score_index = scores.index(min(scores))
            self.choice = moves[min_score_index]
            return min(scores)




# Main Game Loop
def game_loop():
    n = 3  # Board size
    game = TTT_cs170_judge()
    game.create_board(n)
    player1 = Player_1(game)
    player2 = Player_2(game)
    starter = random.randint(0, 1)
    win = False
    if starter == 0:
        print("Player 1 starts.")
        game.display_board()
        while not win:
            player1.my_play()
            win = game.is_winner('X')
            game.display_board()
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break

            player2.my_play()
            win = game.is_winner('O')
            game.display_board()
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
    else:
        print("Player 2 starts.")
        game.display_board()
        while not win:
            player2.my_play()
            win = game.is_winner('O')
            game.display_board()
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
            
            player1.my_play()
            win = game.is_winner('X')
            game.display_board()
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break

game_loop() # Uncomment this line to play the game
