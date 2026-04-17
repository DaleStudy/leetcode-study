class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        visited = set()

        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[left])
                left += 1

            visited.add(s[i])
            max_len = max(max_len, i - left + 1)
        
        return max_len
