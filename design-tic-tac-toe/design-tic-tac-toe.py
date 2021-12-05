class TicTacToe:
    
    def __init__(self, n: int):
        self.n = n 
        self.horizontal = [0] * n
        self.vertical = [0]*n
        self.diag = 0 
        self.anti_diag = 0 

    def move(self, row: int, col: int, player: int) -> int:
        n=self.n
        move=1
        if player == 2:
            move=-1
        self.horizontal[col] += move
        self.vertical[row] += move
        
        if row == col: 
            self.diag += move 
            
        if row + col == (n-1): 
            self.anti_diag += move 
    
        if abs(self.horizontal[col]) == n or abs(self.vertical[row]) == n or abs(self.diag) == n or abs(self.anti_diag) == n: 
        #if abs(self.horiz[col]) == n or abs(self.vert[row])==n or abs(self.diag1)==n or abs(self.diag2)==n:

            return player 
        
        return 0
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)