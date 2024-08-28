# 시간복잡도: O(N)
# 공간복잡도: out 제외시 O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n

        prod = 1
        for i in range(n - 1):
            prod *= nums[i]
            out[i + 1] *= prod

        prod = 1
        for i in range(n - 1, 0, -1):
            prod *= nums[i]
            out[i - 1] *= prod

        return out
