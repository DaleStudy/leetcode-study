"""
Trie-based add and search with wildcard support.

### BFS approach ###

Time Complexity:
    - addWord: O(L), where L is the length of the inserted word.
    - search: O(N), where N is the length of the search word; search with '.' wildcard may lead to O(B^N) in the worst case,
      where B is average branching factor. For ordinary searches (no wildcards), still O(N).

Space Complexity: O(T)
    - T = total number of characters in all inserted words, due to nodes in the trie.
"""

class WordDictionary:

    def __init__(self):
        self.children = dict()
        self.end = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        search = deque([self])
        for ch in word:
            S = len(search)
            for _ in range(S):
                node = search.popleft()
                if ch == '.':
                    for child in node.children.values():
                        search.append(child)
                elif ch in node.children:
                    search.append(node.children[ch])
                    
        return any(node.end for node in search)

"""
Trie-based add and recursive search with wildcard support.

### DFS approach ###

Time Complexity:
    - addWord: O(L), where L is the length of the inserted word.
    - search: Worst case O(B^N), where N is the length of the search word and B is average branching factor if all
      positions are wildcards. Otherwise O(N) for ordinary search.

Space Complexity: O(T)
    - T = total number of characters in all inserted words (trie size), plus call stack space O(N) during search.
"""

class WordDictionary:

    def __init__(self):
        self.children = dict()
        self.end = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node: WordDictionary, index: int) -> bool:
            if index == len(word):
                return node.end
            ch = word[index]
            if ch == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
            elif ch in node.children:
                return dfs(node.children[ch], index + 1)
            return False

        return dfs(self, 0)
