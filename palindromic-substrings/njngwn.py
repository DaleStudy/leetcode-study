class Solution:
    # Time Complexity: O(n^2), n: len(s)
    # Space Complexity: O(1)
    def countSubstrings(self, s: str) -> int:
        cnt = 0

        for i in range(len(s)):
            # odd number
            start, end = i, i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
                cnt += 1

            # even number
            start, end = i, i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
                cnt += 1

        return cnt
