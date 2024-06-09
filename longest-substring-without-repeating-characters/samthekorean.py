# TC : O(n)
# SC : O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        longest_length = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            longest_length = max(longest_length, right - left + 1)

        return longest_length
