# 시간복잡도: ?
# 공간복잡도: O(S)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)

        def dfs(idx):
            if idx in memo:
                return memo[idx]

            if idx == len(s):
                return True

            for word in wordSet:
                l = len(word)
                if s[idx:idx + l] == word:
                    if dfs(idx + l):
                        memo[idx] = True
                        return True

            memo[idx] = False
            return False

        return dfs(0)
