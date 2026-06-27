# - 문제: https://leetcode.com/problems/two-sum/
# - 해설: https://www.algodale.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index, first_num in enumerate(nums):
            for second_index, second_num in enumerate(nums):
                if first_index == second_index:
                    continue
                if first_num + second_num == target:
                    return [first_index, second_index]

        return []

