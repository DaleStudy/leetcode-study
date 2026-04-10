class WordDictionary:

    def __init__(self):
        self.children = {} # key: character, value: WordDictionary node
        self.is_end = False

    # Time Complexity: O(n), n - length of the word
    # Space Complexity: O(N * n), N - number of words, n - length of the word
    def addWord(self, word: str) -> None:
        cur = self

        for char in word:
            if char not in cur.children:
                cur.children[char] = WordDictionary()
            cur = cur.children[char]

        cur.is_end = True

    # Time Complexity: O(26^n), n - length of the word
    # Space Complexity: O(n^2), n - length of the word
    def search(self, word: str) -> bool:
        cur = self

        for i, char in enumerate(word):
            if char == ".":
                for child in cur.children.values():
                    if child.search(word[i + 1:]):
                        return True
                return False
            
            elif char not in cur.children:
                return False
            
            cur = cur.children[char]

        return cur.is_end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
