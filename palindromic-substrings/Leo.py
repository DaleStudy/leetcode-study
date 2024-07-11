class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def helper(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(len(s)):
            result += helper(i, i)
            result += helper(i, i + 1)

        return result

        ## TC: O(n^2), SC: O(1)
