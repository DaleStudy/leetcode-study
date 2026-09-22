# N is the length of s.
# TC: O(N) - each character is added and removed at most once
# SC: O(N) - stores the characters in the current window
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        longest = 0

        for right, char in enumerate(s):
            while char in chars:
                chars.remove(s[left])
                left += 1

            chars.add(char)
            longest = max(longest, right - left + 1)

        return longest
