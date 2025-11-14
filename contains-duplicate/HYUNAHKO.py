class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) >= 1 and len(nums) <= 100000:
            for i in range(0, len(nums)):
                src = nums[i]
                for j in range(i+1, len(nums)):
                    if src == nums[j]:
                        return True
            return False
        return False
    