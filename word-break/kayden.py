# 시간복잡도: O(S*W)
#   S: s의 길이 300 W: worDict 각 단어의 총 길이 20*1000
#       300 * 20*1000 = 6*1e6 (600만)
# 공간복잡도: O(S)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(idx):
            if idx in memo:
                return memo[idx]

            if idx == len(s):
                return True

            for word in wordDict:
                l = len(word)
                if s[idx:idx + l] == word:
                    if dfs(idx + l):
                        memo[idx] = True
                        return True

            memo[idx] = False
            return False

        return dfs(0)
