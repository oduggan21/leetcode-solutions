class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #i am returning list of rows
        board = [[0 for _ in range(n)] for _ in range(n)]
        
        final_list = []

        def checkLeft(board,row,col):
            col = col -1
            while col >= 0:
                if board[row][col] == 1:
                    return False
                col -= 1
            return True

        def topDiagonal(board,row,col):
            row = row -1
            col = col -1
            while row >= 0 and col >= 0:
                if board[row][col] == 1:
                    return False
                row -=1
                col -=1
            return True

        def bottomDiagonal(board,row,col):
            row = row + 1
            col = col -1
            while row < n and col >= 0:
                if board[row][col] == 1:
                    return False
                row += 1
                col -=1
            return True

        def makeBoard(board):
            new_board = []
            for i in range(n):
                string_val = ''
                for j in range(n):
                    if board[i][j]== 1:
                        string_val+='Q'
                    else:
                        string_val +='.'
                new_board.append(string_val)
                string_val = ''
            final_list.append(new_board)
                
        def backtracking(board,col):
            if col == n:
                makeBoard(board)
                return


            for row in range(n):
               

                if checkLeft(board,row,col) and topDiagonal(board,row,col) and bottomDiagonal(board,row,col):
                    board[row][col] = 1
                    backtracking(board,col+1)
                    board[row][col] = 0

        backtracking(board,0)
        return final_list


