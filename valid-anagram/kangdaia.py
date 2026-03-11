from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s와 t가 아나그램인지 확인하는 함수. 
        아나그램은 문자열의 문자들이 동일하지만 순서가 다른 경우를 말함. 대소문자는 구분하지 않지만, 언어마다의 특수 기호 등은 고려해야 함.
        
        방법:
        1. s와 t를 정렬하여 비교; o(nlogn) 시간복잡도
        2. s와 t의 각 문자의 빈도수를 세어 비교; o(n) 시간복잡도
        -> 실제 dict로 구현하기보다 Counter를 사용하면 o(n)에서도 약간 빠르게 구현 가능
        
        * 언어마다의 특수 문자/기호를 고려해야 해, casefold()를 사용.

        Args:
            s (str): 비교할 문자열 1
            t (str): 비교할 문자열 2

        Returns:
            bool: s와 t가 아나그램이면 True, 아니면 False
        """
        return Counter(s.casefold()) == Counter(t.casefold())