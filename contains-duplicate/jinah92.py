class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        keys = set()
        for num in nums:
            if num in keys:
                return True
            else:
                keys.add(num)
        
        return False
