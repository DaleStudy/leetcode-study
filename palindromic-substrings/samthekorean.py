# O(n^2)
# O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        length, total_palindromes = len(s), 0

        def countPalindromes(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        for i in range(length):
            total_palindromes += countPalindromes(i, i + 1)  # even length palindromes
            total_palindromes += countPalindromes(i, i)  # odd length palindromes

        return total_palindromes
