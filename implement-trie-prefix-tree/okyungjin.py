class Trie:

    def __init__(self):
        self.word_set = set()
        self.prefix_set = set()
        

    def insert(self, word: str) -> None:
        if word in self.word_set:
            return

        self.word_set.add(word)

        prefix = ''
        for char in word:
            prefix += char
            self.prefix_set.add(prefix)


    def search(self, word: str) -> bool:
        return word in self.word_set
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix_set
        