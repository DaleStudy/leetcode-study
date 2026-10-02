# TC: O(N)
# SC: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        max_len, left = 1, 0

        for mid in range(n):
            l, r = mid, mid

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if max_len < r - l - 1:
                max_len, left = r - l - 1, l + 1

            l, r = mid, mid + 1

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if max_len < r - l - 1:
                max_len, left = r - l - 1, l + 1

        return s[left:left + max_len]

