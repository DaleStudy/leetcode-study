from collections import Counter
from typing import List
from unittest import TestCase, main


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.solve_3(nums, k)

    """
    Runtime: 82 ms (Beats 87.87%)
    Analyze Complexity: O(n log n)
    most_common의 정렬이 O(n log n)
    Memory: 21.13 MB (Beats 60.35%)
    """
    def solve_1(self, nums: List[int], k: int) -> List[int]:
        return [key for key, value in Counter(nums).most_common(k)]

    """
    Runtime: 88 ms (Beats 62.46%)
    Analyze Complexity: O(n log n)
    counter 생성에 O(n), 정렬에 O(n log n), slicing에 O(k)
    Memory: 21.17 MB (Beats 60.35%)
    """
    def solve_2(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        sorted_counter = sorted(counter.items(), key=lambda item: -item[1])
        return [item[0] for item in sorted_counter[:k]]


    """
    Runtime: 81 ms (Beats 90.60%)
    Analyze Complexity: O(n)
    counter 생성이 O(n), counter_matrix 생성이 O(n), reversed는 O(1), early-return으로 O(k)
    Memory: 22.10 MB (Beats 12.57%)
    """
    def solve_3(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        counter_matrix = [[] for _ in range(len(nums) + 1)]
        for key, val in counter.items():
            counter_matrix[val].append(key)

        result = []
        for num_list in reversed(counter_matrix):
            for num in num_list:
                result.append(num)
                if len(result) >= k:
                    return result
        else:
            return result


class _LeetCodeTCs(TestCase):
    def test_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        output = [1, 2]
        self.assertEqual(Solution.topKFrequent(Solution(), nums, k), output)

    def test_2(self):
        nums = [1]
        k = 1
        output = [1]
        self.assertEqual(Solution.topKFrequent(Solution(), nums, k), output)


if __name__ == '__main__':
    main()
