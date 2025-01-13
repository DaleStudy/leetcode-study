class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        checked = set()

        def dfs(idx):
            if idx in checked:
                return
            checked.add(idx)

            if idx == len(s):
                return True

            for word in wordDict:
                word_len = len(word)
                if s[idx: idx + word_len] == word:
                    if dfs(idx + word_len):
                        return True
            return False

        return dfs(0)
