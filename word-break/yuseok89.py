class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set()
        word_lens = set()

        for word in wordDict:
            word_set.add(word)
            word_lens.add(len(word))

        word_lens = sorted(word_lens)
        visited = set()

        def rec(cur):
            if cur in visited:
                return False

            if len(cur) == 0:
                return True

            for l in word_lens:
                if len(cur) < l:
                    return False

                if cur[0:l] in word_set:
                    if rec(cur[l:]):
                        return True

            visited.add(cur)

            return False

        return rec(s)

