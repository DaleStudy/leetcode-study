from typing import List
from unittest import TestCase, main
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.solveWithMemoization(nums, target)

    """
    Runtime: 3762 ms (Beats 5.00%)
    Time Complexity: O(n ** 2)
        > 크기가 n인 nums 배열을 2중으로 조회하므로 O(n ** 2)

    Memory: 17.42 MB (Beats 61.58%)
    Space Complexity: O(1)
        > 딱히 저장하는 변수 없음 (반환하는 list 제외)
    """
    def solveWithBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

    """
    Runtime: 52 ms (Beats 89.73%)
    Time Complexity: O(n)
        1. nums 배열을 돌며 idx를 저장하는 dict 생성에 O(n)
        2. 첫 숫자를 선택하기 위해 len(nums)를 for문으로 조회하는데 O(n)
        > O(2n) ~= O(n)

    Memory: 19.96 MB (Beats 8.42%)
    Space Complexity: O(n)
        - 크기가 n인 defaultdict 변수 사용
    """
    def solveWithMemoization(self, nums: List[int], target: int) -> List[int]:
        num_to_idx_dict = defaultdict(list)
        for idx, num in enumerate(nums):
            num_to_idx_dict[num].append(idx)

        for i in range(len(nums)):
            first_num = nums[i]
            second_num = target - nums[i]

            if first_num != second_num:
                if not (len(num_to_idx_dict[first_num]) and len(num_to_idx_dict[second_num])):
                    continue
            else:
                if not (2 <= len(num_to_idx_dict[first_num])):
                    continue

            first_idx = num_to_idx_dict[first_num].pop()
            second_idx = num_to_idx_dict[second_num].pop()

            if first_num != second_num:
                return [first_idx, second_idx]
            else:
                return [second_idx, first_idx]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        output = [0, 1]
        self.assertEqual(Solution.twoSum(Solution(), nums, target), output)

    def test_2(self):
        nums = [3,2,4]
        target = 6
        output = [1, 2]
        self.assertEqual(Solution.twoSum(Solution(), nums, target), output)

    def test_3(self):
        nums = [3, 3]
        target = 6
        output = [0, 1]
        self.assertEqual(Solution.twoSum(Solution(), nums, target), output)

    def test_4(self):
        nums = [3, 2, 3]
        target = 6
        output = [0, 2]
        self.assertEqual(Solution.twoSum(Solution(), nums, target), output)


if __name__ == '__main__':
    main()
