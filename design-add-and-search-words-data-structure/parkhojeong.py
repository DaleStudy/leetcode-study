class Node:
    def __init__(self, ch: str, is_end: bool):
        self.ch = ch
        self.is_end = is_end
        self.child: dict[str, Node] = {}

    def get_child(self, ch) -> None:
        if ch in self.child:
            return self.child[ch]

        return None

    def get_all_child(self) -> List[Node]:
        return self.child.values()

    def add_child(self, node):
        self.child[node.ch] = node

class Trie:
    def __init__(self):
        self.root = Node("", False)

    def add_word(self, word) -> None:
        i = 0
        node = self.root
        while i < len(word):
            ch = word[i]
            child_node = node.get_child(ch)
            if child_node:
                node = child_node
                if i == len(word) - 1:
                    node.is_end = True
            else:
                is_end = True if i == len(word) - 1 else False
                child_node = Node(ch, is_end)
                node.add_child(child_node)
                node = child_node

            i += 1

    def search(self, word: str, i, node) -> bool:
        if word[i] == ".":
            child_nodes = node.get_all_child()
        else:
            child_node = node.get_child(word[i])
            if child_node is None:
                return False
            child_nodes = [child_node]

        for child_node in child_nodes:
            if i == len(word) - 1:
                if child_node.is_end is True:
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
        self.trie.add_word(word)

    def search(self, word: str) -> bool:

        return self.trie.search(word, 0, self.trie.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
