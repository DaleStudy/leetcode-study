class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        num_set = {}
        result = -math.inf

        for idx, num in enumerate(nums):
            if idx == 0:
                num_set[idx] = max(nums[0], result)
            else:
                num_set[idx] = max(num, num_set[idx-1] + num)
            tmp_sum = num_set[idx]
            result = max(result, tmp_sum)
        
        return result
