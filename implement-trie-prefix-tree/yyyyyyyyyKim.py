"""
TrieNode: 한 글자를 담는 노드
- children: 자식노드들 저장하는 딕셔너리
- end: 해당 노드에서 단어가 끝나는지 여부
"""
class TrieNode:
    # Trie 노드 초기화
    def __init__(self):
        self.children = {}  # 자식 노드 저장
        self.end = False    # 단어의 끝인지 표시

"""
Trie(트라): Tree기반의 자료구조(Tree자료구조중하나), 문자열 검색을 위한 특수한 Tree 자료구조
- insert: 주어진 word 삽입
- search: 주어진 word가 Trie에 있는지 검색
- startwith: 주어진 prefix로 시작하는 단어가 있는지 확인
"""
class Trie:
    # Trie 자료구조 초기화(루트 노드 생성)
    def __init__(self):
        # Trie의 시작(빈 루트 노드 생성)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root    # 단어 삽입의 시작 위치 = 루트 노드

        # 단어의 글자 하나하나를 Trie에 삽입
        for i in word:
            # 글자가 자식 노드에 없으면 새로운 노드 생성해서 뻗어가기
            if i not in node.children:
                node.children[i] = TrieNode()

            node = node.children[i] # 다음 글자(노드)로 이동

        node.end = True # 단어 삽입 완료, 현재 노드에서 단어의 끝 표시(True)

    def search(self, word: str) -> bool:
        node = self.root

        for i in word:
            # 글자가 자식노드에 존재하지 않으면 False 리턴
            if i not in node.children:
                return False
            
            node = node.children[i] # 다음 글자(노드)로 이동

        # 단어를 다 돌고 마지막 노드가 단어의 끝이면 node.end는 True
        return node.end        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for i in prefix:
            # 글자가 자식노드에 존재하지 않으면 False 리턴
            if i not in node.children:
                return False

            node = node.children[i] # 다음 글자(노드)로 이동

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
