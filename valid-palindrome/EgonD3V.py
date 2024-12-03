from unittest import TestCase, main


class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.solveWithTwoPointer(s)

    """
    Runtime: 43 ms (Beats 68.60%)
    Time Complexity: O(n)
        - s 문자열 iterable 조회하며 연산에 O(n)
        - range(0, length // 2) 조회에 O(n // 2)
        > O(n) + O(n // 2) ~= O(n)

    Memory: 17.02 MB (Beats 54.30%)
    Space Complexity: O(n)
        - 최대 크기가 n인 trimmed_s 변수 할당에 O(n)
        > O(n)
    """
    def solveWithPointer(self, s: str) -> bool:
        trimmed_s = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                trimmed_s += char.lower()

        length = len(trimmed_s)
        for i in range(0, length // 2):
            if trimmed_s[i] != trimmed_s[length - i - 1]:
                return False
        else:
            return True


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        s = "A man, a plan, a canal: Panama"
        output = True
        self.assertEqual(Solution.isPalindrome(Solution(), s), output)

    def test_2(self):
        s = "race a car"
        output = False
        self.assertEqual(Solution.isPalindrome(Solution(), s), output)

    def test_3(self):
        s = " "
        output = True
        self.assertEqual(Solution.isPalindrome(Solution(), s), output)


if __name__ == '__main__':
    main()
