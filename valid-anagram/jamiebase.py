"""
# Approach
문자열 s를 구성하는 문자의 개수를 세는 딕셔너리 word_dict를 만들고,
문자열 t를 순회하며 word_dict에 키가 있는지 확인합니다.
키가 없으면: 에너그램 불가능.
키가 있으면: 값에서 -1하고, 음수인지 확인하여 에너그램 여부를 판별합니다.

# Complexity
- Time complexity: s의 길이가 N이고, t의 길이가 M일 때 O(N+M)

- Space complexity: O(N+M)
"""

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word_dict = defaultdict(int)
        for ch in s:  # O(N)
            word_dict[ch] += 1

        for ch in t:  # O(M)
            if ch not in word_dict:
                return False
            word_dict[ch] -= 1
            if word_dict[ch] < 0:
                return False

        return True
