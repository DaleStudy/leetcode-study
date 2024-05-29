"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/

Solution:
    - Create two lists to store the product of elements from the left and right
    - Multiply the elements from the left and right lists to get the output

    Example:
        nums = [4, 2, 3, 1, 7, 0, 9, 10]

        left is numbers to the left of the current index
        right is numbers to the right of the current index
        from_left is the product of the numbers to the left of the current index
        from_right is the product of the numbers to the right of the current index

        i = 0: (4) 2 3 1 7 0 9 10
        i = 1: 4 (2) 3 1 7 0 9 10
        i = 2: 4 2 (3) 1 7 0 9 10
        i = 3: 4 2 3 (1) 7 0 9 10
        i = 4: 4 2 3 1 (7) 0 9 10
        i = 5: 4 2 3 1 7 (0) 9 10
        i = 6: 4 2 3 1 7 0 (9) 10
        i = 7: 4 2 3 1 7 0 9 (10)

        from_left = [0, 4, 8, 24, 24, 168, 0, 0]
        from_right = [0, 0, 0, 0, 0, 90, 10, 0]
        output = [0, 0, 0, 0, 0, 15120, 0, 0]

Time complexity: O(n)
    - Calculating the product of the elements from the left: O(n)
    - Calculating the product of the elements from the right: O(n)
    - Calculating the output: O(n)
    - Total: O(n)

Space complexity: O(n)
    - Storing the product of the elements from the left: O(n)
    - Storing the product of the elements from the right: O(n)
    - Storing the output: O(n)
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        from_left = [0] * (len(nums))
        from_right = [0] * (len(nums))

        from_left[0] = nums[0]
        from_right[-1] = nums[-1]

        for i in range(1, len(nums) - 1):
            from_left[i] = from_left[i - 1] * nums[i]

        for i in reversed(range(1, len(nums) - 1)):
            from_right[i] = from_right[i + 1] * nums[i]

        output[0] = from_right[1]
        output[-1] = from_left[-2]
        for i in range(1, len(nums) - 1):
            output[i] = from_left[i - 1] * from_right[i + 1]

        return output
