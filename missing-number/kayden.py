# 시간복잡도: O(N)
# 공간복잡도: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n*(n+1)//2
        return total - sum(nums)
