class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, max_len, max_freq = 0, 0, 0

        window = {}
        for end in range(len(s)):
            char = s[end]
            window[char] = window.get(char, 0) + 1
            max_freq = max(max_freq, window[char])

            while (end - start + 1) - max_freq > k:
                left_char = s[start]
                window[left_char] -= 1
                start += 1

            max_len = end - start + 1 if end - start + 1 > max_len else max_len

        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement('ABAB', 2))
