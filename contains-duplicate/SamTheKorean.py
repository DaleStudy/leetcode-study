# TC : O(n) n being a length of nums array and it iterates the nums array once
# SC : O(n) n being a size of nums array
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
