class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        visited = 0 
        for num in nums:
            visited |= (1 << num)
        
        for i in range(len(nums) + 1):
            if (not visited & (1 << i)):
                return i
        return -1