"""
    TC: O(n^2)
    SC: O(1)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)-2):
            left,right = i+1, len(nums)-1
            while left < right:
                three_sum = nums[i]+nums[left]+nums[right]

                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.add((nums[i], nums[left], nums[right]))
                    left,right = left+1, right-1

        return list(result)

