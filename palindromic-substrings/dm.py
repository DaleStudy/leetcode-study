class Solution:
    def countPalindrome(self, s: str, left: int, right: int) -> int:
        result = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1

        return result

    def countSubstrings(self, s: str) -> int:
        total_count = 0

        for i in range(len(s)):
            left = right = i
            total_count += self.countPalindrome(s, left, right)

        for i in range(len(s) - 1):
            left, right = i, i + 1
            total_count += self.countPalindrome(s, left, right)

        return total_count
