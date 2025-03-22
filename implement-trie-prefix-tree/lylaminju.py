# 시간 복잡도:
# - insert(word): O(m)
#   - m은 word의 길이입니다.
#   - 각 문자에 대해 트리를 탐색하거나 새 노드를 추가하므로 O(m) 시간이 걸립니다.
# 
# - search(word): O(m)
#   - m은 word의 길이입니다.
#   - 트리의 각 문자 노드를 탐색하므로 O(m) 시간이 걸립니다.
# 
# - startsWith(prefix): O(m)
#   - m은 prefix의 길이입니다.
#   - 트리의 각 문자 노드를 탐색하므로 O(m) 시간이 걸립니다.
# 
# 공간 복잡도:
# - O(n * m)
#   - n은 트리에 삽입된 단어의 개수입니다.
#   - m은 각 단어의 평균 길이입니다.
#   - 각 단어의 문자에 대해 새로운 노드를 생성하므로 O(n * m) 공간이 필요합니다.


class Trie:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        current = self
        
        for char in word:
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
        
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True
