# 시간복잡도: O(N)
# 공간복잡도: O(N)
class Solution:

    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n + 1)]
        for num in range(1, n + 1):
            ans[num] = ans[num >> 1] + (num & 1)

        return ans
