from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        sorted_nums = sorted(nums)

        for i in range(len(nums) - 2):
            low, high = i + 1, len(nums) - 1
            while low < high:
                three_sum = sorted_nums[i] + sorted_nums[low] + sorted_nums[high]
                if three_sum == 0:
                    answer.add((sorted_nums[i], sorted_nums[low], sorted_nums[high]))
                    low += 1
                    high -= 1
                elif three_sum < 0:
                    low += 1
                elif three_sum > 0:
                    high -= 1
        return list(answer)

