"""
# Intuition
이진탐색으로 찾는다.

# Complexity
- Time complexity: nums의 길이 N일때, O(logN)

- Space complexity: 재귀스택 O(logN)
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, m, r = 0, len(nums) // 2, len(nums) - 1

        def findMinimum(l, m, r):
            if l == m or r == m:
                return min(nums[l], nums[r])

            # 오른쪽 구간
            if nums[m] > nums[r]:
                return findMinimum(m, (m + r) // 2, r)

            # 왼쪽 구간
            return findMinimum(l, (l + m) // 2, m)

        return findMinimum(l, m, r)
