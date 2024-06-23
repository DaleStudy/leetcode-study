class Trie:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = Trie()

            node = node.children[char]

        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True
