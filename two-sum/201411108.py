from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in dictionary and i != dictionary[diff]:
                return [i, dictionary[diff]]
            dictionary[num] = i
