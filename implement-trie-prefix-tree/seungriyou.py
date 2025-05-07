# https://leetcode.com/problems/implement-trie-prefix-tree/

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            curr = curr.children[w]

        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for p in prefix:
            if p not in curr.children:
                return False
            curr = curr.children[p]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
