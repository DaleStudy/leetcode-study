"""
풀이를 보고 공부했습니다.

Solution:
    set을 이용,
    1) addWord 에선 add
    2) search 에선 .을 포함한 모든 글자가 동일한 단어가 있는지 확인

search 
    Time: O(n * w)
    Space: O(1)
"""


class WordDictionary:

    def __init__(self):
        self.root = set()

    def addWord(self, word: str) -> None:
        self.root.add(word)

    def search(self, word: str) -> bool:
        for candidate in self.root:
            if len(candidate) != len(word):
                continue
            if all(w == c or w == "." for w, c in zip(word, candidate)):
                return True
        return False


"""
풀이를 보고 공부했습니다.

Solution: Trie - 달레의 코드
"""


class WordDictionary:

    def __init__(self):
        self.root = {"$": True}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {"$": False}
            node = node[ch]
        node["$"] = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node["$"]

            ch = word[idx]
            if ch in node:
                return dfs(node[ch], idx + 1)
            if ch == ".":
                if any(dfs(node[k], idx + 1) for k in node if k != "$"):
                    return True
            return False

        return dfs(self.root, 0)


"""
풀이를 보고 공부했습니다.

Solution: Trie with TrieNode - NeetCode
"""


class TrieNode:
    def __init__(self):
        self.children = {}  # a: TrieNode
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
