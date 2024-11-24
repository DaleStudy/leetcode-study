'''
풀이
- Trie 자료구조 구현을 따릅니다

Big O
- N: 이전까지 insert한 word의 수
- W: 현재 insert하거나 search하려는 word의 길이
- P: 현재 startsWith하려는 prefix의 길이

- insert
  - Time complexity: O(W)
    - word를 구성하는 모든 문자에 대해 현재 Trie에 저장 여부를 검사합니다
      해시맵 자료구조를 사용하고 있기에 검색과 삽입 모두 constant 시간 복잡도를 가집니다
  - Space complexity: O(W)
    - 최악의 경우 모든 문자를 Trie에 새롭게 추가할 수 있습니다
- search
  - Time complexity: O(W)
    - insert와 같습니다
  - Space complexity: O(1)
- startsWith
  - Time complexity: O(P)
    - search와 같습니다
  - Space complexity: O(1)
'''

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        parent = self.root

        for c in word:
            if c not in parent:
                parent[c] = {}
            parent = parent[c]

        parent["word"] = word

    def search(self, word: str) -> bool:
        parent = self.root

        for c in word:
            if c not in parent:
                return False
            parent = parent[c]
        
        return "word" in parent and parent["word"] == word
        

    def startsWith(self, prefix: str) -> bool:
        parent = self.root

        for c in prefix:
            if c not in parent:
                return False
            parent = parent[c]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
