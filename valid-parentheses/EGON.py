from typing import List
from unittest import TestCase, main


class Solution:
    def isValid(self, s: str) -> bool:
        return self.solveWithStack(s)

    """
    Runtime: 34 ms (Beats 66.54%)
    Time Complexity: O(n)
        > 문자열 s의 길이 L만큼 조회하므로 O(n), early return이 있으므로 upper bound

    Memory: 16.59 MB (Beats 50.97%)
    Space Complexity: O(n)
        - close_p_dict의 크기는 상수로 처리
        > 최대 길이가 L인 배열 stack을 사용했으므로 O(n)
    """
    def solveWithStack(self, s: str) -> bool:
        close_p_dict = {')': '(', '}': '{', ']': '['}
        stack = []
        for curr_p in s:
            if not stack or curr_p not in close_p_dict:
                stack.append(curr_p)
                continue

            if close_p_dict[curr_p] != stack[-1]:
                return False
            else:
                stack.pop()

        return not stack


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        s = "()"
        output = True
        self.assertEqual(Solution.isValid(Solution(), s), output)

    def test_2(self):
        s = "()[]{}"
        output = True
        self.assertEqual(Solution.isValid(Solution(), s), output)

    def test_3(self):
        s = "(]"
        output = False
        self.assertEqual(Solution.isValid(Solution(), s), output)

    def test_4(self):
        s = "([])"
        output = True
        self.assertEqual(Solution.isValid(Solution(), s), output)


if __name__ == '__main__':
    main()
