class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for l in range(0, len(nums)):
                if i == l:
                    continue
                if nums[i] + nums[l] == target:
                    return [i, l]
