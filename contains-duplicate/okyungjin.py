# Time: O(nlogn)
# Space: O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # O(nlogN)

        for idx in range(1, len(nums)): # O(N)
            if nums[idx] == nums[idx-1]:
                return True
        
        return False
