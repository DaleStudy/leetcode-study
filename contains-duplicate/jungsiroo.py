class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Slow - tc : O(n) / sc : O(1)
		
        """return len(set(nums)) != len(nums)"""

        # Fast - tc : O(n) / sc : O(n)
        check = set()
        
        for num in nums:
            if num in check:
                return True
            check.add(num)
        
        return False


        
