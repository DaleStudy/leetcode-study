from unittest import TestCase, main
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.solve_1(s, t)

    """
    Runtime: 46 ms (Beats 71.98%)
    Time Complexity: O(n)
        - 길이가 n인 str s, str t, dict counter를 순회하므로 O(3n) ~= O(n)
    Space Complexity: O(n)
        - 크기가 최대 n인 dict를 변수로 저장하여 사용하므로 O(n) 
    Memory: 16.88 MB (Beats 88.63%)
    """
    def solve_1(self, s: str, t: str) -> bool:
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for char in t:
            counter[char] = counter.get(char, 0) - 1

        return any(counter.values()) is False

    """
    Runtime: 47 ms (Beats 67.45%)
    Time Complexity: O(n)
        - 크기가 n인 Counter 2개를 생성하므로 O(2n) ~= O(n)
    Space Complexity: O(n)
        - 크기가 n인 Counter 2개를 생성하므로 O(2n) ~= O(n)
    Memory: 16.94 MB (Beats 46.26%)
    """
    def solve_2(self, s: str, t: str) -> bool:
        return Counter(s) is Counter(t)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        s = "anagram"
        t = "nagaram"
        output = True
        self.assertEqual(Solution.isAnagram(Solution(), s, t), output)

    def test_2(self):
        s = "rat"
        t = "car"
        output = True
        self.assertEqual(Solution.isAnagram(Solution(), s, t), output)


if __name__ == '__main__':
    main()
