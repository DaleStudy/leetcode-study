# Trie Data Structure 구현
# TC: O(n), SC: O(N)
# autocomplete and spellchecker 등에 사용

class Node:
    def __init__(self, ending=False):
        self.children = {}
        self.ending = ending

class Trie:
    def __init__(self):
        self.root = Node(ending=True)  # 노드 객체 생성

    def insert(self, word: str) -> None:
        node = self.root  #Trie의 최상위 노드부터 시작 
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()  # 새로운 노드 생성
            node = node.children[ch]
        node.ending = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.ending
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
