# TC : O(nlog(n))
# SC : O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        count = 0
        ans = []

        for i in range(n + 1):
            while i > 0:
                count += i % 2
                i = i // 2
            ans.append(count)
            count = 0

        return ans
