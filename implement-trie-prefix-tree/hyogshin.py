"""
풀이 방법
- insert: 입력된 단어의 캐릭터로 for loop을 돌아 node.children에 없는 캐릭터라면 추가하고 있다면 node.isEnd = True
- search: 입력된 단어를 캐릭터 단위로 for loop을 돌고 node.children에 없다면 바로 False 반환, 만약 모든 캐릭터가 있는 경우 단어있는 확인하기 위해 isEnd 체크
- startsWith: 입력된 prefix로 for loop을 돌아 node.children에 없다면 바로 False 반환

시간 복잡도: O(n)
- for loop -> O(n)

공간 복잡도: O(n)
- Trie를 저장하는 공간 -> O(n)
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
      self.root = TrieNode()

    def insert(self, word: str) -> None:
      node = self.root
      for ch in word:
        if ch not in node.children:
          node.children[ch] = TrieNode()
        node = node.children[ch]
      node.isEnd = True
        
    def search(self, word: str) -> bool:
      node = self.root
      for ch in word:
        if ch not in node.children:
          return False
        node = node.children[ch]
      return node.isEnd
            
    def startsWith(self, prefix: str) -> bool:
      node = self.root
      for ch in prefix:
        if ch not in node.children:
          return False
        node = node.children[ch]
      return True

if __name__ == "__main__":
    trie = Trie()

    # insert & search 테스트
    trie.insert("apple")
    print(trie.search("apple"))    # True
    print(trie.search("app"))      # False
    print(trie.startsWith("app"))  # True

    trie.insert("app")
    print(trie.search("app"))      # True

    # 추가 케이스
    trie.insert("application")
    print(trie.search("application"))  # True
    print(trie.startsWith("appl"))     # True
    print(trie.search("apply"))        # False

    trie.insert("bat")
    trie.insert("bath")
    print(trie.search("bat"))      # True
    print(trie.startsWith("ba"))   # True
    print(trie.search("bad"))      # False

