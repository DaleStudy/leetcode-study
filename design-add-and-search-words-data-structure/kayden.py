class Node:
    def __init__(self, ending=False):
        self.ending = ending
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.head = Node(True)

    # 시간복잡도: O(W)
    def addWord(self, word: str) -> None:
        node = self.head

        for ch in word:
            if ch not in node.children:
                node.children.setdefault(ch, Node())
            node = node.children[ch]

        node.ending = True

    # 시간복잡도: O(W*N) W: word 길이 N: 자식 노드의 개수
    def search(self, word: str) -> bool:
        def dfs(idx, node):
            if idx == len(word):
                return node.ending

            if word[idx] == '.':
                for n in node.children.values():
                    if dfs(idx + 1, n):
                        return True
            elif word[idx] in node.children:
                return dfs(idx + 1, node.children[word[idx]])
            else:
                return False

        return dfs(0, self.head)
