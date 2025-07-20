class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining not in my_dict:
                my_dict[nums[i]] = i
            else:
                return [my_dict[remaining], i]
