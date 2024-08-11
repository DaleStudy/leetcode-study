class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True 
            seen.add(num)
        return False