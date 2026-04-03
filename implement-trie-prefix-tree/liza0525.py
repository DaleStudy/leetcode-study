# 7기 풀이
# Trie 전체 공간 복잡도: 공간: O(n * m)
#   - n은 단어 수, m은 평균 단어 길이
# 각 메서드 마다 시간 복잡도와 공간 복잡도 작성
class Node:
    def __init__(self, val=None):
        self.children = {}  # 자식 노드를 담을 dictionary
        self.is_end = False  # 현재 노드를 끝으로 하는 단어가 저장되었는지에 대한 flag


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        # 시간: O(m) — m은 word의 길이, 문자 하나씩 순회
        # 공간: O(m) — 최악의 경우 m개의 새 노드 생성 (아무것도 공유 안할 때)
        node = self.root
        for s in word:
            if s not in node.children:  # 아직 저장이 되지 않은 문자라면 children에 노드로써 저장해둔다.
                node.children[s] = Node(s)
            node = node.children[s]  # 다음 노드를 children node로 지정하여 후손까지 저장할 수 있도록 함
        node.is_end = True  # 모든 노드를 저장한 후에는 단어의 끝을 알리도록 is_end를 True로 변경

    def search(self, word: str) -> bool:
        # 시간: O(m) — m은 word/prefix의 길이만큼 순회
        # 공간: O(1) — 새 노드 생성 없이 포인터만 이동
        node = self.root
        for s in word:
            if s not in node.children:  # 찾으려는 단어의 문자가 저장되어 있지 않으면 search 실패이므로 False 반환
                return False
            node = node.children[s]

        return node.is_end  # 끝까지 돌아보고 해당 단어의 끝이 저장되어 있는지 아닌지를 반환하므로써 search의 성패 여부를 확인할 수 있음

    def startsWith(self, prefix: str) -> bool:
        # start with의 경우에는, search와 거의 로직이 동일하나, is_end의 여부를 볼 필요가 없으므로 모든 문자에 대한 search가 끝나면 무조건 True 반환
        node = self.root
        for s in prefix:
            if s not in node.children:
                return False
            node = node.children[s]

        return True

