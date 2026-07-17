"""
Time Complexity: O(L), where L is the length of the input string (word or prefix) per operation.
Space Complexity: O(N), where N is the total number of characters inserted into the trie (all words inserted).

- Each Trie node uses a dictionary to store children nodes for each character.
- The `end` flag indicates whether the current node represents the end of a complete word.
- The `insert` method adds a word to the trie by sequentially creating/following nodes for each character.
- The `search` method checks for the presence of a full word in the trie by traversing nodes for each character and checking the `end` flag at the last character.
- The `startsWith` method checks if there exists any word in the trie with the given prefix by traversing nodes for each character in the prefix.
"""
class Trie:

    def __init__(self):
        self.children = dict()
        self.end = False

    def insert(self, word: str) -> None:
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]

        node.end = True

    def search(self, word: str, isPrefix: bool = False) -> bool:
        node = self

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True if isPrefix else node.end

    def startsWith(self, prefix: str) -> bool:
        return self.search(word=prefix, isPrefix=True)
