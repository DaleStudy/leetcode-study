import sys
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = -sys.maxsize

        for num in nums:
            max_val = max(max_val, num)

        nums = [x for x in nums if x != 0]
        if not nums:
            return max_val

        arr = []
        arr.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] * nums[i - 1] > 0:
                arr[-1] += nums[i]
            else:
                arr.append(nums[i])

        for num in arr:
            max_val = max(max_val, num)

        while len(arr) >= 2:
            if arr[0] < 0:
                arr = arr[1:]
            if arr[-1] < 0:
                arr = arr[:-1]

            max_val = max(max_val, arr[0])
            if len(arr) >= 2:
                arr[1] = arr[0] + arr[1]
                arr = arr[1:]

            max_val = max(max_val, arr[-1])
            if len(arr) >= 2:
                arr[-2] = arr[-1] + arr[-2]
                arr = arr[:-1]

        max_val = max(max_val, arr[0])

        return max_val
