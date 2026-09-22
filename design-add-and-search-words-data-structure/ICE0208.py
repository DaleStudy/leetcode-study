class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            # 패턴을 모두 확인했을 때 실제 단어의 끝인지 확인한다.
            if index == len(word):
                return node.is_end

            char = word[index]

            # '.'은 현재 노드의 모든 자식 문자와 대응될 수 있다.
            if char == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True

                return False

            # 일반 문자는 해당 자식 노드만 확인한다.
            child = node.children.get(char)

            if child is None:
                return False

            return dfs(index + 1, child)

        return dfs(0, self.root)
