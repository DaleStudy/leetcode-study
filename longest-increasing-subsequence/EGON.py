from typing import List
from unittest import TestCase, main


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.solve_with_Memo_BS(nums)

    """
    Runtime: 68 ms (Beats 86.42%)
    Time Complexity: O(n)
        - nums 배열 조회에 O(n)
        - 최악의 경우 num의 모든 원소에 대해 bisect_left 실행가능, O(log n) upper bound
        > O(n) * O(log n) ~= O(n * log n)

    Memory: 16.92 MB (Beats 29.49%)
    Space Complexity: O(n)
        > 최대 크기가 n인 lis 배열 사용에 O(n)
    """
    def solve_with_Memo_BS(self, nums: List[int]) -> int:

        def bisect_left(lis: List[int], target: int):
            lo, hi = 0, len(lis)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if lis[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        lis = []
        for num in nums:
            if not lis:
                lis.append(num)
                continue

            if lis[-1] < num:
                lis.append(num)
            else:
                lis[bisect_left(lis, num)] = num

        return len(lis)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        prices = [10,9,2,5,3,7,101,18]
        output = 4
        self.assertEqual(Solution.lengthOfLIS(Solution(), prices), output)


if __name__ == '__main__':
    main()
