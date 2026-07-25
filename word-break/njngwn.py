from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def check(cur):
            if cur == len(s):
                return True
            for word in wordDict:
                if s[cur: cur + len(word)] == word:
                    if check(cur + len(word)):
                        return True
            return False

        return check(0)
