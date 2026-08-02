class Node:
    def __init__(self):
        self.is_end = False
        self.children: dict[str, Node] = {}

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()

            node = node.children[ch]

        node.is_end = True

    def search(self, word: str) -> bool:

        return self._search(word, 0, self.root)

    def _search(self, word: str, i: int, node: Node) -> bool:
        if i == len(word):
            return node.is_end

        if word[i] == ".":
            children_nodes = node.children.values()
        else:
            node = node.children.get(word[i])
            if node is None:
                return False
            children_nodes = [node]

        for node in children_nodes:
            if self._search(word, i + 1, node):
                return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
