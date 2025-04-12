class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, num in enumerate(nums):
            if target - num in temp:
                return [i, temp[target - num]]
            temp[num] = i
        return None
