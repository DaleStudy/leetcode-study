class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = {}
        for i in range(len(nums)):
            if target-nums[i] in num_list:
                return [num_list[target-nums[i]], i]
            num_list[nums[i]] = i
    
