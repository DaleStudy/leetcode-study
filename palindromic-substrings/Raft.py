class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.countPalindrome(s, i, i)
            count += self.countPalindrome(s, i, i + 1)
        return count
    
    def countPalindrome(self, s, l, r):
        count = 0
        while r < len(s) and l >= 0 and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
# T: O(n^2)
# S: O(n^2)

