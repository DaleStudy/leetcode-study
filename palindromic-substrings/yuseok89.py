# TC: O(N^2)
# SC: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:

        ans = 0
        n = len(s)

        for center_idx in range(n):

            idx = 0

            while 0 <= center_idx - idx and center_idx + idx < n:
                if s[center_idx - idx] == s[center_idx + idx]:
                    ans = ans + 1
                else:
                    break

                idx += 1

            idx = 0
            while 0 <= center_idx - idx and center_idx + idx + 1< n:
                if s[center_idx - idx] == s[center_idx + idx + 1]:
                    ans = ans + 1
                else:
                    break

                idx += 1

        return ans

