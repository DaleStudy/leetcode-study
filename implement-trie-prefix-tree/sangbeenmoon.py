class Trie:

    children = {}
    is_end = False

    def __init__(self):
        self.children = {}
        self.is_end = False
        return

    def insert(self, word: str, i=0) -> None:

        if i == len(word):
            self.is_end = True
            return

        target = word[i]

        if target in self.children:
            node = self.children[target]
            node.insert(word, i+1)
        else:
            node = Trie()
            node.insert(word, i+1)
            self.children[target] = node
        
    def search(self, word: str, i=0) -> bool:

        if i == len(word):
            return self.is_end

        target = word[i]

        if target in self.children:
            node = self.children[target]
            return node.search(word, i+1)
        else:
            return False
        

    def startsWith(self, prefix: str, i=0) -> bool:
        if i == len(prefix):
            return True

        target = prefix[i]

        if target in self.children:
            node = self.children[target]
            return node.startsWith(prefix, i+1)
        else:
            return False        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
