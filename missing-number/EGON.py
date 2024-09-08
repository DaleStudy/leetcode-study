from typing import List
from unittest import TestCase, main


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return self.solveWithSet(nums)

    """
    Runtime: 118 ms (Beats 31.19%)
    Time Complexity:
        - 크기가 n + 1인 List를 set로 변환에 O(n + 1)
        - nums 배열 조회하며 set.remove에 O(n) * O(1) ~= O(n)
        - 마지막 set에서 pop하는데 O(1)
        > O(n + 1) + O(n) + O(1) ~= O(n)

    Memory: 18.56 MB (Beats 5.%)
    Space Complexity:
        - 크기가 n + 1인 set 사용에 O(n + 1)
        > O(n + 1) ~= O(n)
    """
    def solveWithSet(self, nums: List[int]) -> int:
        range_set = set(range(0, len(nums) + 1))
        for num in nums:
            range_set.remove(num)

        return range_set.pop()


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [3, 0, 1]
        output = 2
        self.assertEqual(Solution.missingNumber(Solution(), nums), output)

    def test_2(self):
        nums = [0, 1]
        output = 2
        self.assertEqual(Solution.missingNumber(Solution(), nums), output)

    def test_3(self):
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        output = 8
        self.assertEqual(Solution.missingNumber(Solution(), nums), output)


if __name__ == '__main__':
    main()
