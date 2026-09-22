class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        max_len = 0

        def idx(ch):
            return ord(ch) - ord('A')

        left = 0
        for i in range(len(s)):
            freq[idx(s[i])] += 1
            window_size = i - left + 1
            size = window_size - max(freq)

            while size > k:
                freq[idx(s[left])] -= 1

                left += 1
                window_size -= 1
                size = window_size - max(freq)

            max_len = max(max_len, window_size)

        return max_len

