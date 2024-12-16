from unittest import TestCase, main


class Solution:
    def reverseBits(self, n: int) -> int:
        return self.solve(n)

    """
    Runtime: 32 ms (Beats 80.50%)
    Time Complexity: O(1)
        - n을 str로 변환하는데, n은 32 bit 정수이므로 O(32), upper bound
        - zfill로 문자열의 길이를 32로 맞추는데, O(32), upper bound
        - 문자열을 뒤집는데 마찬가지로, O(32), upper bound
        - 뒤집은 문자열을 정수로 변환하는데 문자열에 비례하며 이 길이는 최대 32이므로, O(32), upper bound
        > O(32) * O(32) * O(32) * O(32) ~= O(1)

    Memory: 16.50 (Beats 64.72%)
    Space Complexity: O(1)
        - 각 단계마다 최대 길이가 32인 문자열이 임시로 저장되므로 O(32) * 4
        > O(32) * 4 ~= O(1)
    """
    def solve(self, n: int) -> int:
        return int(str(n).zfill(32)[::-1], 2)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        n = int("00000010100101000001111010011100")
        output = 964176192
        self.assertEqual(Solution.reverseBits(Solution(), n), output)


if __name__ == '__main__':
    main()
