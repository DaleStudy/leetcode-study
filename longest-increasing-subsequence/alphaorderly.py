"""
Time Complexity: O(n log n)
Space Complexity: O(n)

### Binary search approach ###

For each number in nums:
    - Find the insertion position for num in arr to maintain sorted order (binary search).
    - If num is greater than all elements in arr, append it (extend the LIS).
    - Otherwise, replace the element at position with num to keep tails as small as possible.
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []

        for num in nums:
            position = bisect_left(arr, num)
            if position == len(arr):
                arr.append(num)
            else:
                arr[position] = num

        return len(arr)
