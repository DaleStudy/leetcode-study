class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        ch_to_idx = {}
        start_idx = 0

        i = 0
        length_of_longest_substring = 1
        for i in range(len(s)):
            ch = s[i]
            if ch in ch_to_idx and ch_to_idx[ch] >= start_idx:
                start_idx = ch_to_idx[ch] + 1
                ch_to_idx[ch] = i
            else:
                ch_to_idx[ch] = i
                length_of_substring = i - start_idx + 1
                length_of_longest_substring = max(length_of_longest_substring, length_of_substring)

        return length_of_longest_substring

