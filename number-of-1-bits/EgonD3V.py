from unittest import TestCase, main


class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.solve_4(n=n)

    """
    Runtime: 26 ms (Beats 97.13%)
    Analyze Complexity: O(log n), bin(int)가 O(log(n))
    Memory: 16.56 MB (Beats 22.67%)
    """
    def solve_1(self, n: int) -> int:
        return bin(n).count('1')

    """
    Runtime: 31 ms (Beats 85.00%)
    Analyze Complexity: O(log n)
    Memory: 16.60 MB (Beats 22.67%)
    """
    def solve_2(self, n: int) -> int:
        hamming_weight = 0
        while n:
            hamming_weight += n % 2
            n = n >> 1
        return hamming_weight

    """
    Runtime: 30 ms (Beats 88.73%)
    Analyze Complexity: O(k), k는 2진수의 1의 갯수 (== O(log(n)))
    Memory: 16.56 MB (Beats 22.67%)
    """
    # Brian Kernighan's Algorithm
    def solve_3(self, n: int) -> int:
        hamming_weight = 0
        while n:
            n &= (n - 1)
            hamming_weight += 1
        return hamming_weight

    """
    Runtime: 36 ms (Beats 53.56%)
    Analyze Complexity: O(k), k는 2진수의 1의 갯수 (== O(log(n)))
    Memory: 16.55 MB (Beats 22.67%)
    """
    def solve_4(self, n: int) -> int:
        hamming_weight = 0
        while n:
            hamming_weight += n & 1
            n >>= 1
        return hamming_weight


class _LeetCodeTCs(TestCase):
    def test_1(self):
        n = 11
        output = 3
        self.assertEqual(Solution.hammingWeight(Solution(), n=n), output)

    def test_2(self):
        n = 128
        output = 1
        self.assertEqual(Solution.hammingWeight(Solution(), n=n), output)

    def test_3(self):
        n = 2147483645
        output = 30
        self.assertEqual(Solution.hammingWeight(Solution(), n=n), output)


if __name__ == '__main__':
    main()
