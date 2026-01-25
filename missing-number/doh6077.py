# Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # First Solution: Time Complexity: O(n^2)
        n = len(nums)

        for i in range(0,n + 1):
            if i not in nums:
                return i    
            
        # Time Complexity: O(n) 
        n = len(nums)
        # calculate the sum of first n numbers
        sum_val = n * (n + 1) // 2
        return sum_val - sum(nums)

