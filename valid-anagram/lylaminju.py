from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Python의 collections.Counter는 유니코드 문자를 지원합니다.
# 시간복잡도: O(n)
    # Counter는 해시 테이블 기반의 연산으로 동작하며, 각 문자열의 문자를 한 번씩 순회합니다.
# 공간복잡도: O(n)
    # 각 문자열에 대해 Counter 객체를 생성하므로, 최악의 경우 각 문자마다 빈도를 저장하는 데 O(n) 크기의 해시테이블이 필요합니다.
