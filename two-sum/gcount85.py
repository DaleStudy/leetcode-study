"""
- Approach:
  Make a dictionary.
  The key is difference from target and the value is its index,
  then iterate the number array and with its value, find the key in the dictionary.
- Time Complexity: O(2N) => O(N)
- Space complexity: O(N)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i, v in enumerate(nums):  # O(N)
            num_dic[target - v] = i

        for i, v in enumerate(nums):  # O(N)
            if v in num_dic and num_dic[v] != i:
                return [num_dic[v], i]
