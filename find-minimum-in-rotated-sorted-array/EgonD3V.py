from typing import List
from unittest import TestCase, main


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.solve_binary_search(nums)

    """
    Runtime: 32 ms (Beats 97.56%)
    Time Complexity: O(log n)
        - 크기가 n인 배열에 대한 이분탐색에 O(log n)
            - while 조건문 판단에 O(2), and 연산이므로 단축 평가에 의해 upper bound
        - 엣지 케이스 처리를 위한 마지막 lo, hi 2개 항에 대한 min연산에 O(2)
        > O(log n) * O(2) + O(2) ~= O(log n)

    Memory: 16.82 (Beats 50.00%)
    Space Complexity: O(1)
        > 이분탐색에 필요한 정수형 변수 lo, hi, mid 3개만 사용했으므로 n과 상관없이 O(1)
    """
    def solve_binary_search(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi and nums[hi] < nums[lo]:
            mid = (lo + hi) // 2
            if nums[lo] < nums[mid]:
                lo = mid
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                break

        return min(nums[lo], nums[hi])


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [2, 1]
        output = 1
        self.assertEqual(Solution().findMin(nums), output)


if __name__ == '__main__':
    main()
