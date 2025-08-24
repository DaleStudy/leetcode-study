class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.links = {}


class Trie:

    def __init__(self):
        self._root = TrieNode()

    def _recurAdd(self, node: TrieNode, word: str) -> None:
        if not word:
            node.isEnd = True
            return

        ch = word[0]
        # 부모 노드의 자식에 있는지 확인
        next_link = node.links.get(ch)

        if not next_link:
            node.links[ch] = TrieNode()
            next_link = node.links[ch]

        self._recurAdd(next_link, word[1:])

    def insert(self, word: str) -> None:
        if not word:
            return

        self._recurAdd(self._root, word)

    def _recurSearch(self, node: TrieNode, word: str) -> bool:
        if not word:
            return node.isEnd

        ch = word[0]
        next_link = node.links.get(ch)
        if next_link:
            return self._recurSearch(next_link, word[1:])
        return False

    def search(self, word: str) -> bool:
        if not word:
            return False

        return self._recurSearch(self._root, word)

    def startsWith(self, prefix: str) -> bool:
        node = self._root
        for ch in prefix:
            if ch not in node.links:
                return False
            node = node.links[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
