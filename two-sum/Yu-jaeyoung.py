class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexed_nums = sorted(enumerate(nums), key=lambda x: x[1])

        left = 0
        right = len(indexed_nums) - 1

        while left < right:
            current_sum = indexed_nums[left][1] + indexed_nums[right][1]

            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [indexed_nums[left][0], indexed_nums[right][0]]

        return []

