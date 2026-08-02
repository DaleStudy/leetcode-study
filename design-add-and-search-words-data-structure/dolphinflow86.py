# TC: L is len(word), M is the total number of nodes in the tree.
#   addWord: O(L)
#   search: O(L) - wildcard '.' appears at most 2 times, so max branching is 26^2 which is a constant. if the wildcard can appear indefinitely, O(min(26^L, M))

# SC:
#   addWord: O(L)
#   search: O(D) where D is depth of the tree.

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]

        cur.is_end = True

    def dfs(self, node, depth, word) -> bool:
        if not node: return False
        if len(word) == depth: return node.is_end
        
        ch = word[depth]
        if ch == '.':
            for child in node.children:
                if self.dfs(child, depth+1, word):
                    return True
        else:
            idx = ord(ch) - ord('a')
            next_node = node.children[idx]
            if next_node:
                if self.dfs(next_node, depth+1, word):
                    return True

        return False

    def search(self, word: str) -> bool:
        return self.dfs(self.root, 0, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
