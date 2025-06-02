class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        
        def backtracking(node,word):
            if node is None:
                return False
            if not word:
                return node.endOfWord
            c = word[0]
            if c == '.':
                for i in range(26):
                    if backtracking(node.children[i], word[1:]):
                        return True
                return False
            else:
                index= ord(c) - ord('a')
                child =  node.children[index]
                if not child:
                    return False
                return backtracking(node.children[index], word[1:])
                
     
            
        return backtracking(self.root, word)
                
