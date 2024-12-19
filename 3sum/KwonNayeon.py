"""
Constraints:
1. 3 <= nums.length <= 3000
2. -10^5 <= nums[i] <= 10^5

Time Complexity:
    - O(n^2) (정렬은 O(n log n), 이중 반복문은 O(n^2))
Space Complexity:
    - O(n) (결과 리스트)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
    
        return result
