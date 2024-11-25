from unittest import TestCase, main
from typing import List
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.solve_3(nums=nums)

    """
    Runtime: 412 ms (Beats 75.17%)
    Analyze Complexity: O(n)
    Memory: 31.92 MB (Beats 45.93%)
    """
    def solve_1(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    """
    Runtime: 423 ms (Beats 39.66%)
    Analyze Complexity: O(n)
    Memory: 34.54 MB (Beats 14.97%)
    """
    def solve_2(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num in counter:
                return True
            else:
                counter[num] = True
        else:
            return False

    """
    Runtime: 441 ms (Beats 16.59%)
    Analyze Complexity: O(n)
    Memory: 34.57 MB (Beats 14.97%)
    """
    def solve_3(self, nums: List[int]) -> bool:
        return Counter(nums).most_common(1)[0][1] > 1


class _LeetCodeTCs(TestCase):
    def test_1(self):
        nums = [1, 2, 3, 1]
        output = True
        self.assertEqual(Solution.containsDuplicate(Solution(), nums=nums), output)

    def test_2(self):
        nums = [1, 2, 3, 4]
        output = False
        self.assertEqual(Solution.containsDuplicate(Solution(), nums=nums), output)

    def test_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        output = True
        self.assertEqual(Solution.containsDuplicate(Solution(), nums=nums), output)


if __name__ == '__main__':
    main()
