class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie

        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]

        cur[0] = True

    def search(self, word: str) -> bool:

        n = len(word)

        def rec(cur, idx):
            if idx == n:
                return 0 in cur

            if word[idx] == '.':
                for next in cur:
                    if next == 0:
                        continue
                    if rec(cur[next], idx + 1):
                        return True
                return False
            else:
                if word[idx] in cur:
                    return rec(cur[word[idx]], idx + 1)
                else:
                    return False

        return rec(self.trie, 0)

