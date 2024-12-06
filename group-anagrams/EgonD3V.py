from typing import List
from unittest import TestCase, main


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.solveWithHashableKey(strs)

    """
    Runtime: 88 ms (Beats 65.68%)
    Time Complexity: 
        - strs의 길이 n 만큼 조회에 O(n)
        - string을 key로 변환하는데 string의 길이 L에 대해 O(L * log L) * O(L)
            - string의 최대 길이는 100이므로 O(100 * log 100) * O(100)가 upper bound
        - anagram_dict 갱신에 O(1)
        - 최대 크기가 n인 anagram_dict.values()를 list로 변환하는데 O(n^2)
        > O(n) * O(L * log L) * O(L) + O(n^2) ~= O(n^2)

    Memory: 19.32 MB (Beats 95.12%)
    Space Complexity: O(n * L)
        - 최대 n개의 key-value pair를 가질 수 있는 anagram_dict 사용, upper bound
          anagram_dict의 value는 최대 길이 L인 List[str] 이므로 O(n * L)
        > O(n * L)
    """
    def solveWithHashableKey(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for string in strs:
            key = ''.join(sorted(string))
            anagram_dict[key] = anagram_dict.get(key, []) + [string]

        return list(anagram_dict.values())


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        output = [["bat"],["nat","tan"],["ate","eat","tea"]]
        self.assertEqual(Solution.groupAnagrams(Solution(), strs), output)

    def test_2(self):
        strs = [""]
        output = [[""]]
        self.assertEqual(Solution.groupAnagrams(Solution(), strs), output)

    def test_3(self):
        strs = ["a"]
        output = [["a"]]
        self.assertEqual(Solution.groupAnagrams(Solution(), strs), output)


if __name__ == '__main__':
    main()
