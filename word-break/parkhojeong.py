class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_len_set = set(len(word) for word in wordDict)
        word_set = set(word for word in wordDict)
        visited = set()

        def dfs(s: str):
            if len(s) == 0:
                return True

            if s in visited:
                return False

            visited.add(s)

            for word_len in word_len_set:
                if s[:word_len] not in word_set:
                    continue

                if dfs(s[word_len:]):
                    return True

            return False

        return dfs(s)
