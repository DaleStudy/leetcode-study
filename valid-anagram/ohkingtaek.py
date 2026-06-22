from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        두 문자열이 anagram인지 확인한다.
        Counter를 사용하여 각 문자열의 문자 빈도수를 계산하고 비교한다.
        시간복잡도 O(n), 문자열을 한 번 순회하여 빈도수를 계산
        """
        return True if Counter(s) == Counter(t) else False
