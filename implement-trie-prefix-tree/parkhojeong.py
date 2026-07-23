class Node:
    def __init__(self, s: str):
        self.isLast: bool = False
        self.childs: dict[str, Node] = {}

    def addChild(self, s: str):
        if self.getChild(s) is not None:
            return

        node = Node(s)
        self.childs[s] = node

    def getChild(self, s: str) -> Node | None:
        if s not in self.childs:
            return None

        return self.childs[s]

    def setIsLast(self, isLast: bool):
        self.isLast = isLast

    def getIsLast(self) -> bool:
        return self.isLast


class Trie:
    root: Node

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            ch = word[i]
            if node.getChild(ch) is None:
                node.addChild(ch)

            node = node.getChild(ch)
            if i == len(word) - 1:
                node.setIsLast(True)

    def findNode(self, word) -> Node | None:
        node = self.root
        for ch in word:
            node = node.getChild(ch)
            if node is None:
                return None

        return node

    def search(self, word: str) -> bool:
        node = self.findNode(word)
        if node is None or not node.getIsLast():
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        return self.findNode(prefix) is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
