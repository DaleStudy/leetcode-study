class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        pointer = self.root
        for char in word:
            if char in pointer:
                pointer = pointer[char]
                continue
            else:
                pointer[char] = dict()
                pointer = pointer[char]
        pointer[0] = dict()

    def search(self, word: str) -> bool:
        pointer = self.root
        for char in word:
            if char in pointer:
                pointer = pointer[char]
                continue
            else:
                return False
        if 0 in pointer:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for char in prefix:
            if char in pointer:
                pointer = pointer[char]
                continue
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
