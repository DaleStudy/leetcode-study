class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        if len(nums) >= 2 and len(nums) <= 1e4:
            for idx1, i in enumerate(nums):
                num1 = i
                for idx2 in range(idx1+1, len(nums)):
                    num2 = nums[idx2]
                    if ((num1 + num2) == target):
                        result.append(idx1)
                        result.append(idx2)
                        return result
