class Node:
    ch = ""
    is_end = False
    child: List[Node] = None
    child: dict[str, Node] = None

    def __init__(self, ch, is_end):
        self.ch = ch
        self.is_end = is_end
        self.child = {}

    def getIsEnd(self):
        return self.is_end

    def setIsEndTrue(self):
        self.is_end = True

    def getChild(self, ch) -> None:
        if ch in self.child:
            return self.child[ch]

        return None

    def getAllChild(self) -> List[Node]:
        return self.child.values()

    def addChild(self, node):
        self.child[node.ch] = node

class Trie:
    def __init__(self):
        self.root = Node("", False)

    def addWord(self, word) -> None:
        i = 0
        node = self.root
        while i < len(word):
            ch = word[i]
            child_node = node.getChild(ch)
            if child_node:
                node = child_node
                if i == len(word) - 1:
                    node.setIsEndTrue()
            else:
                is_end = True if i == len(word) - 1 else False
                child_node = Node(ch, is_end)
                node.addChild(child_node)
                node = child_node

            i += 1

    def search(self, word: str, i, node) -> bool:
        if word[i] == ".":
            child_nodes = node.getAllChild()
        else:
            child_node = node.getChild(word[i])
            if child_node is None:
                return False
            child_nodes = [child_node]

        for child_node in child_nodes:
            if i == len(word) - 1:
                if child_node.getIsEnd() is True:
                    return True
                else:
                    continue

            if self.search(word, i + 1, child_node):
                return True

        return False


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.addWord(word)

    def search(self, word: str) -> bool:

        return self.trie.search(word, 0, self.trie.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
