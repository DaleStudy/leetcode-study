from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time complexity O(n)
        Space complexity O(1)

        Sliding window
        """
        start, end = 0, 0
        window = defaultdict(int)
        max_len = 0

        while end < len(s):
            window[s[end]] += 1
            while end-start+1 - max(window.values()) > k:
                window[s[start]] -= 1
                start += 1
            # move idx
            max_len = max(max_len, end-start+1)
            end += 1

        return max_len
