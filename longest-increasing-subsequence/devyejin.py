from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(target):
            left, right = 0, len(result)

            while left < right:
                mid = (left + right) // 2
                if result[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        result = []

        for num in nums:
            idx = binary_search(num)
            if idx == len(result):
                result.append(num)
            else:
                result[idx] = num

        return len(result)



