class Solution:
    # Time Complexity: O(n), n: len(s)
    # Space Complexity: O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_len, max_cnt = 0, 0
        left = 0

        for right in range(len(s)):  # window expands
            ch = ord(s[right]) - ord('A')
            count[ch] += 1
            max_cnt = max(max_cnt, count[ch])

            # len(substring) - len(most frequent character) > k => window needs to schrink
            if (right - left + 1) - max_cnt > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
