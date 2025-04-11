"""
시간 복잡도: O(N)
공간 복잡도: O(N)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(len(nums) - 1):
            prefix[i + 1] = prefix[i] * nums[i]
        
        suffix = [1] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            suffix[i - 1] = suffix[i] * nums[i]
        
        result = []
        for i, j in zip(prefix, suffix):
            result.append(i * j)
        
        return result
