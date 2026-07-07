from collections import Counter


class Solution_2:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        n = len(s), m = len(t)

        두 문자열의 각 문자 개수를 센 뒤 비교한다.

        시간 복잡도: O(n + m)
        공간 복잡도: O(1)
        - 입력 문자가 알파벳 소문자 26개로 제한되기 때문
        """
        return Counter(s) == Counter(t)


class Solution_01:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        n = len(s), m = len(t)

        두 문자열을 각각 정렬한 뒤 비교한다.

        시간 복잡도: O(n log n + m log m)
        공간 복잡도: O(n + m)
        """
        return sorted(s) == sorted(t)
