from typing import *


class Solution:
    """
    풀이:
    s와 t 길이가 다르면 anagram 아니므로 False로 early return
    set으로 s의 중복 문자 제거
    set을 순회하면서 각 문자가 s와 t에서 등장하는 횟수가 동일한지 확인
    다르면 False, 끝까지 통과하면 True

    TC: O(n+m)
      - if len(s) != len(t): O(1)
      - ss = set(s): O(n)
      - for c in ss: 최대 26회 반복 → O(1)
        - s.count(c): O(n)
        - t.count(c): O(m)
      - 최종: O(n+m)

    SC: O(n)
      - ss = set(s): 최악의 경우 O(n)
      - 그 외 상수: O(1)
      - 최종: O(n)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ss = set(s)
        for c in ss:
            if s.count(c) != t.count(c):
                return False

        return True
