"""
Solution:
    Use a hash map to store numbers and their indices
    Iterate through the list and check if difference between target and val 
    return the index list

Time: O(n)
Space: O(n)

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # num : index

        for i, val in enumerate(nums):
            diff = target - val
            if diff in num_map:
                return [num_map[diff], i]
            num_map[val] = i
