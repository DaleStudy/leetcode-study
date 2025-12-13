
# 208. Implement Trie (Prefix Tree)
class Trie:

    def __init__(self):
        self.list = []
        

    def insert(self, word: str) -> None:
        self.list.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.list:
            return True
        else:
            return False 
        

    def startsWith(self, prefix: str) -> bool:
        for i, value in enumerate(self.list):
            if value.startswith(prefix):
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
