"""
https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s, e = 0, len(nums) - 1
        arr = [[n, i] for i, n in enumerate(nums)]

        arr.sort(key=lambda x: x[0])

        while s <= e:
            now = arr[s][0] + arr[e][0]
            if now == target:
                return [arr[s][1], arr[e][1]]
            if now < target:
                s += 1
            else:
                e -= 1
