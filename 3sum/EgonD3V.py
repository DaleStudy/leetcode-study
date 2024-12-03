from typing import List
from unittest import TestCase, main


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.solveWithTwoPointer(nums)

    """
    Runtime: 691 ms (Beats 62.42%)
    Time Complexity: O(n^2)
        - nums를 정렬하는데 O(n * log n)
        - 첫 index를 정하기 위해 range(len(nums) - 2) 조회하는데 O(n - 2)
        - i + 1 부터 n - 1까지 lo, hi 투포인터 조회하는데, i가 최소값인 0인 경우를 upper bound로 계산하면 O(n - 1)
        > O(n * log n) + O(n - 2) * O(n - 1) ~= O(n * log n) + O(n^2) ~= O(n^2)

    Memory: 20.71 MB (Beats 30.94%)
    Space Complexity:
        - num는 정렬하긴 했는데 자기자신 그대로 사용하므로 계산 외
        > lo나 hi나 triplet_sum은 input에 영향없는 크기의 메모리를 사용하므로 O(1)
    """

    def solveWithTwoPointer(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if 1 <= i and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                triplet_sum = nums[i] + nums[lo] + nums[hi]

                if triplet_sum < 0:
                    lo += 1
                elif triplet_sum > 0:
                    hi -= 1
                else:
                    triplets.append([nums[i], nums[lo], nums[hi]])

                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1

                    lo += 1
                    hi -= 1

        return triplets


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        output = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(Solution.threeSum(Solution(), nums), output)

    def test_2(self):
        nums = [0, 1, 1]
        output = []
        self.assertEqual(Solution.threeSum(Solution(), nums), output)

    def test_3(self):
        strs = [0, 0, 0]
        output = [[0, 0, 0]]
        self.assertEqual(Solution.threeSum(Solution(), strs), output)

    def test_4(self):
        strs = [0, 0, 0, 0, 0, 0, 0, 0]
        output = [[0, 0, 0]]
        self.assertEqual(Solution.threeSum(Solution(), strs), output)


if __name__ == '__main__':
    main()
