"""
[문제풀이]
# Inputs

# Outputs

# Constraints

# Ideas

[회고]

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        counter = {}
        start, end = 0, 0
        while end < len(s):
            counter[s[end]] = counter.get(s[end], 0) + 1
            while end - start + 1 - max(counter.values()) > k:
                counter[s[start]] -= 1
                start += 1
            max_len = max(end - start + 1, max_len)
            end += 1
        return max_len

