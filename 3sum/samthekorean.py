# O(n^2) where there is nested loop.
# O(1) where high and low are reused as constant values.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize a set to store unique triplets
        triplets = set()

        # Sort the list to make two-pointer approach possible
        nums.sort()

        # Iterate through the list, considering each element as a potential first element of a triplet
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1

            # To avoid duplicate iteration
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]

                if three_sum < 0:
                    low += 1
                elif three_sum > 0:
                    high -= 1
                else:
                    triplets.add((nums[i], nums[low], nums[high]))
                    low += 1
                    high -= 1
