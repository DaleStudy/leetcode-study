"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Solution: 
    - Initialize the Trie class with an empty list of words.
    - Insert a word by appending it to the list of words.
    - Search for a word by checking if it is in the list of words.
    - Check if a prefix exists by iterating through the list of words and checking if any word starts with the prefix.

Tiem complexity: 
    - Insert: O(1)
        - Appending to a list is O(1)
    - Search: O(n)
        - Searching for an element in a list is O(n)
    - StartsWith: O(n)
        - Iterating through a list is O(n)

Space complexity: O(n)
    - The list of words may have all the words in the trie.
"""


class Trie:
    def __init__(self):
        self.words = []

    def insert(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        for word in self.words:
            if word.startswith(prefix):
                return True

        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
