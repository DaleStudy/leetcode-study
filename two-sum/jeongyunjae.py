class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, data in enumerate(nums):
            remaining = target - data
            if remaining not in my_dict:
                my_dict[data] = i
            else:
                return [my_dict[remaining], i]
