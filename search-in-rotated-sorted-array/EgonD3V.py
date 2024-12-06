from typing import List
from unittest import TestCase, main


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.solve_binary_search(nums, target)

    """
    Runtime: 4 ms (Beats 100.00%)
    Time Complexity: O(log n)
    > nums를 이진탐색으로 조회하므로 O(log n)

    Memory: 17.03 MB (Beats 10.00%)
    Space Complexity: O(1)
    > index를 위한 정수형 변수만 사용하므로 O(1)
    """
    def solve_binary_search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1

            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid

        return lo if nums[lo] == target else -1


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        output = 4
        self.assertEqual(Solution.search(Solution(), nums, target), output)

    def test_2(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        output = -1
        self.assertEqual(Solution.search(Solution(), nums, target), output)

    def test_3(self):
        nums = [1]
        target = 0
        output = -1
        self.assertEqual(Solution.search(Solution(), nums, target), output)

    def test_4(self):
        nums = [3, 1]
        target = 1
        output = 1
        self.assertEqual(Solution.search(Solution(), nums, target), output)


if __name__ == '__main__':
    main()
