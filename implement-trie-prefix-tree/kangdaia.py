class Node:
    """
    Trie 자료구조의 노드를 나타내는 클래스.
    
    key: 노드의 키 (문자)
    data: 노드에 저장된 데이터 (단어)
    children: 자식 노드들을 저장함 (키: 문자, 값: Node 객체)
    """
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    """
    Trie 자료구조를 구현한 클래스.
    
    head: Trie의 루트 노드

    insert(word): 단어를 Trie에 삽입하는 메서드
    search(word): Trie에서 단어가 존재하는지 확인하는 메서드
    startsWith(prefix): Trie에서 접두사가 존재하는지 확인하는 메서드
    
    - 시간 복잡도: O(M) (M은 단어의 길이)
    - 공간 복잡도: O(N * M) (N은 단어의 개수, M은 단어의 최대 길이)
    """
    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        curr.data = word

    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True if curr.data == word else False

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
