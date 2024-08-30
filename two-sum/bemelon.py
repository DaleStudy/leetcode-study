class Solution:
    # Space complexity: O(n)
    # Time complexity: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_index = {} 
        for curr, num in enumerate(nums): 
            rest = target - num 
            if rest in num_index: 
                return [num_index[rest], curr]
            else: 
                num_index[num] = curr 
        return [0, 0]

