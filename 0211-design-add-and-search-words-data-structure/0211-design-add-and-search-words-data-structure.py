class Node:
    
    def __init__(self):
        
        self.d = defaultdict(Node)
        self.EOW = False
        

class WordDictionary:
    
    def __init__(self):
        self.words = Node()
        

    def addWord(self, word: str) -> None:
        
        cur = self.words
        for ch in word: cur = cur.d[ch]
        cur.EOW = True


    def search(self, word: str) -> bool:
        
        return self.dfs(word, self.words)   

    
    def dfs(self, word: str, node: Node, i = 0) -> bool:
        
        if not node         : return False
        if i == len(word)   : return node.EOW

        if word[i] == '.'   : return any(
                                (self.dfs(word, child, i+1)
                                for child in node.d.values()))

        return self.dfs(word, node.d.get(word[i]), i+1)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)