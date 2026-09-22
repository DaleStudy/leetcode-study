# TC: O(L)
# SC: O(L * N)
class TrieNode:
    def __init__(self):
        self.next = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.next:
                cur.next[c] = TrieNode()

            cur = cur.next[c]

        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.next:
                return False

            cur = cur.next[c]

        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.next:
                return False

            cur = cur.next[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

