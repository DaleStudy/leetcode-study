class TrieNode:
    def __init__(self):
        # 다음 문자로 연결되는 자식 노드
        self.children = {}

        # 현재 노드에서 하나의 완성된 단어가 끝나는지 표시
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # 모든 단어 탐색이 시작되는 최상위 노드
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root

        # 단어의 각 문자를 따라가며 경로를 생성한다.
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()

            current_node = current_node.children[char]

        # 마지막 노드에 단어의 끝임을 표시한다.
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        last_node = self._find_last_node(word)

        # 경로가 존재하고, 마지막 노드에서 단어가 끝나야 한다.
        return (
            last_node is not None
            and last_node.is_end_of_word
        )

    def startsWith(self, prefix: str) -> bool:
        # 접두사는 해당 경로가 존재하기만 하면 된다.
        return self._find_last_node(prefix) is not None

    def _find_last_node(self, text: str):
        current_node = self.root

        # 문자열의 각 문자를 따라 마지막 노드까지 이동한다.
        for char in text:
            if char not in current_node.children:
                return None

            current_node = current_node.children[char]

        return current_node
