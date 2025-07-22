class Solution(object):
    def twoSum(self, nums, target):

        nums_tuple = sorted(list(enumerate(nums)), key=lambda x: x[1])
        left, right = 0, len(nums) - 1

        while left < right:
            temp_sum = nums_tuple[left][1] + nums_tuple[right][1]
            if temp_sum == target:
                return [nums_tuple[left][0], nums_tuple[right][0]]
            elif temp_sum < target:
                left += 1
            else:
                right -= 1

