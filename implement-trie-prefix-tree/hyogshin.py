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
