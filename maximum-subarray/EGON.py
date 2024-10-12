from typing import List
from unittest import TestCase, main


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.solve_divide_and_conquer(nums)

    """
    Runtime: 548 ms (Beats 38.42%)
    Time Complexity: O(n)
        - nums를 조회하는데 O(n)
            - max_sum을 갱신하는데 2개 항에 대한 max연산에 O(2)
            - max_subarray_sum을 갱신하는데 2개 항에 대한 max 연산에 O(2)
        > O(n) * (O(2) + O(2)) = O(4 * n) ~= O(n)

    Memory: 30.96 MB (Beats 74.82%)
    Space Complexity: O(1)
        > 정수형 변수, 실수형 변수 하나 씩만 사용했으므로 O(1)
    """
    def solve_kadane(self, nums: List[int]) -> int:
        max_subarray_sum, result = 0, float('-inf')
        for num in nums:
            max_subarray_sum = max(num, max_subarray_sum + num)
            result = max(max_subarray_sum, result)
        return result

    """
    Runtime: 732 ms (Beats 5.04%)
    Time Complexity: O(n * log n)
        - max_prefix_sum에서 deepcopy에 O(n), 계산에 O(n)
        - max_suffix_sum에서 deepcopy에 O(n), 계산에 O(n)
        - divide_and_sum에서 재귀 호출 depth가 log n, 호출 결과의 최대 갯수는 n이므로, 일반적인 divide and conquer의 시간복잡도와 동일한 O(n * log n)
        > 2 * O(n) + 2 * O(n) + O(n * log n) ~= O(n * log n)

    Memory: 68.75 MB (Beats 20.29%)
    Space Complexity: O(n)
        - max_prefix_sum에서 O(n)
        - max_suffix_sum에서 O(n)
        > O(n) + O(n) = 2 * O(n) ~= O(n)
    """
    def solve_divide_and_conquer(self, nums: List[int]) -> int:
        max_prefix_sum = nums[::]
        for i in range(1, len(nums)):
            max_prefix_sum[i] = max(max_prefix_sum[i], max_prefix_sum[i - 1] + nums[i])

        max_suffix_sum = nums[::]
        for i in range(len(nums) - 2, -1, -1):
            max_suffix_sum[i] = max(max_suffix_sum[i], max_suffix_sum[i + 1] + nums[i])

        def divide_and_sum(nums: List[int], left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            return max(
                divide_and_sum(nums, left, mid),
                max_prefix_sum[mid] + max_suffix_sum[mid + 1],
                divide_and_sum(nums, mid + 1, right)
            )

        return divide_and_sum(nums, 0, len(nums) - 1)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        output = 6
        self.assertEqual(Solution.maxSubArray(Solution(), nums), output)

    def test_2(self):
        nums = [1]
        output = 1
        self.assertEqual(Solution.maxSubArray(Solution(), nums), output)

    def test_3(self):
        nums = [5,4,-1,7,8]
        output = 23
        self.assertEqual(Solution.maxSubArray(Solution(), nums), output)

    def test_4(self):
        nums = [-4, -3, -2, -1]
        output = -1
        self.assertEqual(Solution.maxSubArray(Solution(), nums), output)


if __name__ == '__main__':
    main()
