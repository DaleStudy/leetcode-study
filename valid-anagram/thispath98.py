
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time Complexity:
            O(N log N):
                두 string을 정렬, 이는 보통 quick sort로 구현되어
                N log N 만큼 소요된다.

        Space Complexity:
            O(N):
                최악의 경우 (모든 string이 유일할 경우) N개의 리스트
                를 저장한다.
        """
        return sorted(s) == sorted(t)

    def isAnagramCounter(self, s: str, t: str) -> bool:
        """
        Time Complexity:
            O(N):
                해시를 기반으로 일치 여부 탐색, N개의 엔트리를
                한번씩 순회하는 것으로 구현된다.

        Space Complexity:
            O(N):
                최악의 경우 (모든 string이 유일할 경우) N개의 리스트
                를 저장한다.
        """
        from collections import Counter

        return Counter(s) == Counter(t)
