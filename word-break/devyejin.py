from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(subs: str):
            if subs in memo:
                return memo[subs]

            if not subs:
                return True

            for word in wordDict:
                if subs.startswith(word):
                    if dfs(subs[len(word):]):
                        memo[subs] = True
                        return True

            memo[subs] = False
            return False

        memo = {}
        return dfs(s)

