# 문제내용
# 두 문자열 s와 t가 주어질 때, t가 s의 애너그램(anagram)인지 판별하라.
# 애너그램이란 같은 문자를 같은 개수만큼 사용해 순서만 바꾼 문자열을 말해.
# 결과: 애너그램이면 True, 아니면 False.

# sorted(): 문자열을 한 글자씩 잘라 오름차순 정렬해서 비교 (간단, 직관)
# 1. sorted()로 두 문자열을 정렬해서 비교
# 2. 정렬된 경과가 같으면 True 아니면 False
# 시간복잡도: O(n log n)
# 공간복잡도: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
