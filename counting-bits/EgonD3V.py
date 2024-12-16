from typing import List
from unittest import TestCase, main


class Solution:
    def countBits(self, n: int) -> List[int]:
        return self.solve_1(n)

    """
    Runtime: 78 ms (Beats 31.22%)
    Time Complexity: O(n * log n), 크기가 n인 배열의 원소들에 대해 시행마다 크기가 2로 나누어지는 비트연산을 수행하므로
    Space Complexity: O(1), 변수 저장 없이 바로 결과 반환
    Memory: 23.26 MB (Beats 39.52%)
    """
    def solve_1(self, n: int) -> List[int]:
        def count_number_of_1(n: int):
            count = 0
            while n:
                n &= (n - 1)
                count += 1
            return count

        return [count_number_of_1(num) for num in range(n + 1)]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        n = 2
        output = [0, 1, 1]
        self.assertEqual(Solution.countBits(Solution(), n), output)

    def test_2(self):
        n = 5
        output = [0, 1, 1, 2, 1, 2]
        self.assertEqual(Solution.countBits(Solution(), n), output)


if __name__ == '__main__':
    main()
