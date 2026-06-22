class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "AABABBA", 1
        # l = 0
        # r = 4
        # max_freq = 0
        # max_len = 4
        # {"A":1, "B":2}

        l = 0
        max_len = 0
        max_freq = 0
        seen = {}

        for r, char in enumerate(s):
            seen[char] = seen.get(char, 0) + 1
            max_freq = max(max_freq, seen[char])

            while (r - l + 1) - max_freq > k:
                seen[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
        return max_len

# Time Complexity: O(n)
# Space Complexity: O(1)
