'''
이번 문제는 Trie 자료구조를 활용한 문제였습니다.
이를 파악하지 못해서 전체 탐색하는 구조를 만들었다 결국 또 도움을 받아 이해하는 것에 목표를 뒀습니다.
'''
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
                return any(dfs(node[k], idx + 1) for k in node if k != "$")
            return False
        return dfs(self.root, 0)
