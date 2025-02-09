"""
Recursive vs Iterative

재귀 방식의 경우, 만약 문자열의 길이가 굉장히 길다면 그만큼의 콜이 일어나고 이는 성능적으로 느려질 수 있음.
두 가지 모두 시간 복잡도 면에서는 O(m) 임 (m = len(string))

Node 클래스를 따로 두어 처리하면 가독성 높게 처리할 수 있다.
"""

class Node:
    def __init__(self, key=None):
        self.key = key
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr = self.head

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node(ch)
            curr = curr.children[ch]
        curr.is_end = True
    
    def search(self, word: str) -> bool:
        curr = self.head
        
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        
        return curr.is_end
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.head

        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
        
