class Solution:
    """
    Ideation:
        애너그램은 문자열 내 배치만 다를 뿐, 동일한 문자들이 동일한 카운트로 보장되어야 한다.
        이를 위해 문자 기준으로 정렬하고 같은지 확인합니다.
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)