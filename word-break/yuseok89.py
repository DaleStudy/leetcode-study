#TC: O()
#SC: O()
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set()

        max_len = 0
        min_len = 300

        for word in wordDict:
            word_set.add(word)
            max_len = max(max_len, len(word))
            min_len = min(min_len, len(word))

        v = set()

        def rec(cur):
            if cur in v:
                return False

            v.add(cur)

            if len(cur) == 0:
                return True

            for l in range(min_len, max_len + 1):
                if len(cur) < l:
                    return False

                if cur[0:l] in word_set:
                    if rec(cur[l:]):
                        return True

            return False

        return rec(s)

