from typing import Dict


class Trie:
    def __init__(self):
        self.children: Dict[str, "Trie"] = {}
        self.is_end_of_word: bool = False

    def insert(self, word: str) -> None:
        node: Trie = self

        for char in word:
            if char not in node.children:
                node.children[char] = Trie()

            node = node.children[char]

        node.is_end_of_word = True


class WordDictionary:
    def __init__(self):
        self.trie: Trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        def searchInNode(node: Trie, word: str) -> bool:
            for i, char in enumerate(word):
                if char == ".":
                    # If the current character is '.', check all possible nodes at this level
                    for child in node.children.values():
                        if searchInNode(child, word[i + 1 :]):
                            return True

                    return False
                else:
                    # If the current character is not in the children, return False
                    if char not in node.children:
                        return False

                    node = node.children[char]

            return node.is_end_of_word

        return searchInNode(self.trie, word)
