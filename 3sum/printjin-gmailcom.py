class Solution:
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            low, high = i + 1, len(nums) - 1
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                if three_sum < 0:
                    low += 1
                elif three_sum > 0:
                    high -= 1
                else:
                    triplets.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low, high = low + 1, high - 1
        return triplets
