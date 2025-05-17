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
            elif ch == ".":
                return any(dfs(node[k], idx + 1) for k in node if k != "$")
            else:
                return False
        return dfs(self.root, 0)
