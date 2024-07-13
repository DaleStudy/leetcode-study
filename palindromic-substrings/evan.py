class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_around_center(left: int, right: int) -> int:
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        total_count = 0

        for i in range(len(s)):
            # Odd-length palindromes (single character(s[i]) center)
            total_count += expand_around_center(i, i)
            # Even-length palindromes (two character(s[i], s[i+1])s center)
            total_count += expand_around_center(i, i + 1)

        return total_count
