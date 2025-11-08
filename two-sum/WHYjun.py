class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in memo:
                # Each input would have exactly one solution
                return [memo[diff], i]
            memo[num] = i    
            
        return []
