# 시간복잡도 : O(N)
# 공간복잡도 : O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0]
        local_sum = nums[0]

        for i in range(1, len(nums)):
            local_sum = max(nums[i], local_sum + nums[i])
            global_sum = max(local_sum, global_sum)

        return global_sum

