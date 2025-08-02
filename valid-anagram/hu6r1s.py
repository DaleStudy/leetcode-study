from collections import defaultdict

class Solution:
    """
        1. Counter를 이용한 풀이
            - Counter로 풀이하였으나 s, t 길이가 서로 다를 때 해결되지 않음
        2. defaultdict 활용 풀이
            - 똑같이 개수 세고 제외
        
        TC
        - s의 길이: n, t의 길이: n (조건상 같거나 비교 가능한 길이)
        - 첫 번째 for 루프: O(n) → s의 모든 문자를 순회
        - 두 번째 for 루프: O(n) → t의 모든 문자를 순회
        - 총 시간 복잡도 = O(n)

        SC
        - counter는 알파벳 개수를 세는 용도로만 사용됨
        - 공간 복잡도 = O(1)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)
        
        for i in s:
            counter[i] += 1
        
        for i in t:
            if i not in counter:
                return False
            counter[i] -= 1

            if counter[i] == 0:
                del counter[i]
        return False if counter else True
