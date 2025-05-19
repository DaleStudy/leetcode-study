"""
Time complexity O(n)
"""

class Node:
    def __init__(self, end=False):
        self.children = {} # hash table
        self.end = end

class Trie:
    def __init__(self):
        self.root = Node(end=True)

    def insert(self, word: str) -> None:
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        if node.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
