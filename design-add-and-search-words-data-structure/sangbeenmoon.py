class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

        

    def addWord(self, word: str, i=0) -> None:
        if i >= len(word):
            self.is_end = True
            return

        target_char = word[i]

        if target_char in self.children:
            node = self.children[target_char]
            node.addWord(word, i+1)
        else:
            node = WordDictionary()
            self.children[target_char] = node
            node.addWord(word, i+1)
        

    def search(self, word: str, i=0) -> bool:
        if i >= len(word):
            return self.is_end

        target_char = word[i]

        if target_char == ".":
            for child_node in self.children.values():
                if child_node.search(word,i+1) == True:
                    return True
            
        if target_char in self.children:
            node = self.children[target_char]
            return node.search(word, i+1)
        else:
            node = WordDictionary()
            return node.search(word, i+1)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
