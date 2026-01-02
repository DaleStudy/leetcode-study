class Solution:
    # TC O(n^2)
    # SC O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        n = len(s)
        for left in range(n):
            saw = set()
            for right in range(left, n):
                if s[right] in saw:
                    break
                else:
                    saw.add(s[right])
                    max_size = max(max_size, right - left + 1)
        
        return max_size
