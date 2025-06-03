class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def addWord(word):
            curr = self.root
            for c in word:
                index= ord(c)-ord('a')
                if not curr.children[index]:
                    curr.children[index]= TrieNode()
                curr = curr.children[index]
            curr.endOfWord = True

        for word in words:
            addWord(word)
        
        final_list = set()

        def backtracking(r,c,node,word):
            if board[r][c] == '.':
                return
            index = ord(board[r][c]) - ord('a')
            if node.children[index] is not None:
                word += board[r][c]
                node = node.children[index]
                if node.endOfWord:
                    final_list.add(word) 
               
                temp = board[r][c]
                board[r][c] = '.'
                if r > 0:
                    backtracking(r-1, c,node,word)
                if r<len(board)-1:
                    backtracking(r+1,c,node,word)
                if c > 0:
                    backtracking(r,c-1,node,word)
                if c < len(board[0])-1:
                    backtracking(r,c+1,node,word)
                board[r][c] = temp
            else:
                return
        

        
        curr = self.root
        for row in range(len(board)):
            for col in range(len(board[0])):
                backtracking(row,col,curr,'')
        return list(final_list)
            

            
