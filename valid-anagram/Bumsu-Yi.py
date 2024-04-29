"""
https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict1 = {}
        my_dict2 = {}

        for char in s:
            my_dict1[char] = my_dict1.get(char, 0) + 1

        for char in t:
            my_dict2[char] = my_dict2.get(char, 0) + 1

        return my_dict1 == my_dict2
