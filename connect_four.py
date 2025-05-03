


class ConnectFour: # Connect Four game class
    def __init__(self, height=6, width=7): # Initialize the game board, columns and rows
        self.height= height
        self.width = width
        self.board=[[" "]*width for row in range(height)] #> lisi of list #2D, one row and for each colm in the row, there is a list of 0s
    
    def draw_board(self):

        print([str(i+1) for i in range(self.width)], end="\n\n") # for each column in the board, print the curret index,one arguement to modify the index
        for row in self.board:
            print(row) # print the board

    def get_column(self, index):
        return[row[index] for row in self.board] # return the column of the board
    
    def get_row(self, index):
        return self.board[index]
    
    # def get_diagonals(self):
    #     diagonals =[] # create an empty list for the diagonals

    #     for i in range(self.height + self.width -1):
    #         diag1, diag2 = [], [] # create two empty lists for the diagonals
    #         for j in range (max(i - self.height + 1 ,0), min(i +1, self.height)):
    #             diag1.append(self.board[self.height -1 + j -1][j]) # append the diagonal elements to the list
    #             diag2.append(self.board[i - j][j]) # append the diagonal elements to the list
    #         diagonals.append(diag1)
    #         diagonals.append(diag2)

    def get_diagonals(self):
        diagonals = []

    # Top-left to bottom-right diagonals
        for p in range(self.height + self.width - 1):
            diag = []
            for q in range(max(p - self.width + 1, 0), min(p + 1, self.height)):
                r = p - q
                if r < self.width:
                    diag.append(self.board[q][r])
        diagonals.append(diag)

    # Bottom-left to top-right diagonals
        for p in range(-(self.height - 1), self.width):
            diag = []
            for q in range(self.height):
                r = p + q
                if 0 <= r < self.width:
                    diag.append(self.board[q][r])
        diagonals.append(diag)

        return diagonals


        # return diagonals # return the diagonals of the board
    
    def insert_token(self, team, col):
        if " " not in self.get_column(col):
            return False # if the column is full, return false
        
        row = self.height -1
        while self.board[row][col] != " ":
            row -= 1
        self.board[row][col] = team # team is the token in the board
        return True # insert the token in the board
    
    def check_win(self):
        four_in_row = (["0","0","0","0"], ["1","1","1","1"]) 
        # check rows
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.get_row(row)[col:col+4] in four_in_row:  # extract sequence of four values
                    return True

        # check columns
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.get_column(col)[row:row+4] in four_in_row:
                   return True

        # check diagonals
        for diag in self.get_diagonals():
            for index, _ in enumerate(diag):
                if diag[index:index+4] in four_in_row:
                    return True
                
        return False # if no four in a row, return false
    
    def play(self):
        team = "0"
        # game loop
        while True:
            self.draw_board()
            col = int(input(f"Team {team} choose a column: ")) - 1 # ask user for input
            ok = self.insert_token(team, col)
            while not ok:
                print("Column is full, try again")
                col = int(input(f"Team {team} choose a column: ")) - 1
                ok = self.insert_token(team, col)

            if self.check_win():
                self.draw_board()
                print(f"Team {team} wins!")
                break

            team = "1" if team == "0" else "0"