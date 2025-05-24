class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        def backtracking(r, c, i):

            if i == len(word):
                return True
            if r >= rows or r < 0 or c < 0 or c >= cols:
                return False
            if board[r][c] != word[i]:
                return False
            
            temp= board[r][c]
            board[r][c] = '#'

            if(backtracking(r+1,c,i+1) or
            backtracking(r,c+1, i+1) or
            backtracking(r-1,c,i+1) or
            backtracking(r, c-1, i+1)):
                found = True
            else:
                found = False
            board[r][c] = temp
            
            return found
    
        for i in range(rows):
            for j in range(cols):
                if backtracking(i, j, 0):
                    return True
        return False

    
