class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pos = set()
        pos.add(0)
        len_s = len(s)

        while len(pos) > 0 :
            l = pos.pop()
            for word in wordDict:
                if s[l:].startswith(word):
                    pos.add(l+len(word))
            if l == len_s:
                return True
        return False
