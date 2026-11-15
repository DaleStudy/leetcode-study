class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            seen.add(num)

        if(len(seen) != len(nums)):
            return True
        
        return False
        