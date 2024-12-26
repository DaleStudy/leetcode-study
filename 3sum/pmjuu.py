from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # sort nums before using two-pointers
        
        for i, num in enumerate(nums):
            # skip duplicated targets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -num
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([num, nums[left], nums[right]])

                    # skip duplicated numbers ( ex. nums = [-3 0 0 0 3 3] )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return result
    

# Time Complexity: O(n^2)
# - Sorting takes O(n log n).
# - The outer loop runs O(n) times, and the two-pointer approach inside runs O(n) for each iteration.
# - Combined, the overall time complexity is O(n^2).

# Space Complexity: O(k)
# - The result list uses O(k) space, where k is the number of unique triplets in the output.
