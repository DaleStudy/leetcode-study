"""
Time complexity O(26^w)
Space complexity O(w)

Trie, DFS
"""

class Node:
    def __init__(self, end=False):
        self.children = {} # char : node
        self.end = end

class WordDictionary:

    def __init__(self):
        self.root = Node(end=True)
        
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)

    def dfs(self, start, word):
        ch = word[0]
        if ch == word:
            if ch == '.':
                return any([node.end for node in start.children.values()])
            elif ch in start.children:
                if start.children[ch].end:
                    return True
            return False
        
        if ch == '.':
            return any([self.dfs(node, word[1:]) for c, node in start.children.items()])
        elif ch in start.children:
            return self.dfs(start.children[ch], word[1:])
        else:
            return False
