class trieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isendword = False
class Trie:

    def __init__(self):
        self.root = trieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = trieNode()
            curr = curr.children[index]
        curr.isendword=True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index]:
                curr = curr.children[index]
                continue
            else:
                return False
        
        if curr.isendword:
            return True
        return False
            
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index]:
                curr = curr.children[index]
                continue
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
