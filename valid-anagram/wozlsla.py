"""
# Intuition
애너그램 : 순서만 변경. 요소/개수 동일 -> 비교하여 같은지 확인

# Approach
해시테이블의 키-값(요소-개수) 쌍으로 저장
- 직접 순회 : python interpreter 실행 및 get 메서드 반복 호출/업데이트
- Counter : 문자열을 순회하며 각 문자의 빈도수를 계산하는 과정이 최적화(C)되어 있기 때문에, 파이썬으로 직접 반복문을 작성하는 것보다 훨씬 빠르게 동작

# Complexity
- Time complexity: O(N+M)
- Space complexity: O(K). 사실상 O(1) -> 영어 알파벳 문자열의 경우 K는 26으로 상수에 가까움

"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


""" 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # table_s = table_t = {} # '동일 객체를 참조'하기 때문에 가변 객체의 경우 수정 시 모두 반영 됨.
        table_s = {}
        table_t = {}

        for i in s:
            table_s[i] = table_s.get(i, 0) + 1
        for e in t:
            table_t[e] = table_t.get(e, 0) + 1

        return table_s == table_t

s = "anagram"
t = "nagaram"

# print(Solution.isAnagram(s, t)) -> 클래스 메서드처럼 호출하고 있어서 self를 자동 전달하지 못함

# 클래스 인스턴스화 필요
sol = Solution()
print(sol.isAnagram(s, t))
"""
