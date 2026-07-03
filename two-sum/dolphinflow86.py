# 1) Using nested for loop to find every possible combination for target sum
# TC: O(n^2) where n is the size of nums
# SC: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]
        
        return []

#2) Using two pass approach with hash map so that find out complement with index.
# TC: O(2*n) -> O(n) where n is the size of nums
# SC: O(n) where n is the size of nums
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for i in range(len(nums)):
            seen[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen and i != seen[complement]:
                return [seen[complement], i]
        
        return []

# 3) Tiny optimize from two pass version. Instead of inserting separately, insert within one loop
# TC: O(n), where n is the size of nums
# SC: O(n), where n is the size of nums
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
                
            seen[nums[i]] = i
        
        return []
