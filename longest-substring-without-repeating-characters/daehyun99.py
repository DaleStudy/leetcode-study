class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        longest = 0

        for c in s:
            if c not in seen:
                seen.add(c)
                longest = max(longest, len(seen))
            else:
                while c in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(c)
        return longest
