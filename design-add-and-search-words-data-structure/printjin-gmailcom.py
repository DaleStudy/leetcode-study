class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            ch = word[index]
            if ch == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            if ch in node.children:
                return dfs(index + 1, node.children[ch])
            return False

        return dfs(0, self.root)
