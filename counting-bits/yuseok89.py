# TC: O(N)
# SC: O(N)
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []

        upper = 1
        ans.append(0)

        for idx in range(1, n + 1):
            ans.append(ans[idx - upper] + 1)

            if idx == upper:
                upper *= 2

        return ans

