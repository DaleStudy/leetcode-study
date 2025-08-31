class WordDictionary:

    def __init__(self):
        self.root = {"$": False}

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
                return node.get("$", False)

            ch = word[idx]

            if ch == ".":
                for key in node:
                    if key == "$":
                        continue
                    if dfs(node[key], idx + 1):
                        return True
                return False
            else:
                if ch in node:
                    return dfs(node[ch], idx + 1)
                else:
                    return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

