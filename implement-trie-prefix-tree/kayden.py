class Node:

    def __init__(self, ending=False):
        self.children = {}
        self.ending = ending

# 공간복잡도: O(w*l) w: 단어 수 l: 단어의 평균 길이
class Trie:

    def __init__(self):
        self.head = Node(ending=True)

    # 시간복잡도: O(N)
    def insert(self, word: str) -> None:
        node = self.head
        for ch in word:
            if ch not in node.children:
                node.children.setdefault(ch, Node())
            node = node.children[ch]
        node.ending = True

    # 시간복잡도: O(N)
    def search(self, word: str) -> bool:
        node = self.head
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.ending

    # 시간복잡도: O(N)
    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True
