"""
https://leetcode.com/problems/valid-anagram/description/
두 문자열이 애너그램인지 확인하는 함수를 작성하세요.
애너그램이란 두 문자열이 중복된 알파벳을 같은 개수만큼 포함하고 있는 것을 의미합니다.

TC: O(n)
SC: O(k), k = 알파벳 개수
"""

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def makeMap(s: str):
            str_map = defaultdict(int)
            for char in s:
                str_map[char] += 1
            return str_map

        return makeMap(s) == makeMap(t)


"""
정렬 풀이

TC: O(nlogn)
SC: O(1)
"""
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

"""
Counter 사용 풀이

TC: O(n)
SC: O(k)
"""
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
