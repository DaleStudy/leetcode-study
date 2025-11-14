from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)
"""
================================================================================
풀이 과정 - 08:27 시작 ~ 08:32 종료 (5분 소요)
================================================================================

1. s, t 문자열이 주어지는데
2. s와 t가 anagram이면 True, 그렇지 않으면 False 반환
3. anagram이란 어떤 단어나 구의 글자들을 모두 한 번씩만 사용하여 순서를 바꾸어 새롭게 만든 단어나 구
4. 그러면 문자 정렬을 해서 같은지 비교를 하는 방법이 있을 것 같고
5. 근데 그렇게 하면 문자 정렬에 시간 복잡도가 증가하니까
6. 각 문자의 개수를 카운팅하는 해싱 Counter를 이용해서
7. 서로의 키 값이 동일한지 확인한다거나 하면 조금 더 빠르게 처리가 가능할듯?


[1차 시도] 반복문으로 직접 비교
────────────────────────────────────────────────────────────────────────────────
8. Counter로 각 문자의 개수를 세서 비교하는 방식 구현

    if len(s) != len(t):
        return False
    s_count = Counter(s)
    t_count = Counter(t)

    for key, value in s_count.items():
        if value != t_count[key]:
            return False
    return True

9. 정상적으로 통과되는 것 확인 완료


[2차 개선] Counter 객체 직접 비교
────────────────────────────────────────────────────────────────────────────────
10. Counter 객체끼리 직접 비교가 가능하다는 것을 알게 됨
11. 반복문 제거하고 더 간결하게 개선

    if len(s) != len(t):
        return False

    return Counter(s) == Counter(t)

12. 코드가 더 간결해지고 가독성도 향상됨
13. 최종 통과 확인 완료
14. 근데 그럼에도 len 길이를 비교하는것은 O(1) 측면에서 좋다는 답변도 받음

[다른 풀이 탐구] Counter를 사용하지 않고 직접 딕셔너리를 만들어서 처리한다면?
────────────────────────────────────────────────────────────────────────────────
        counter = {}
        if len(s) != len(t):
            return False

        for char in s:
            counter[char] = counter.get(char,0) + 1

        for char in t:
            counter[char] = counter.get(char,0) - 1
            if counter[char] < 0:
                return False

        return True

[다른 풀이 탐구] s와 t는 소문자만 받아올 수 있는데 그러면, 배열로 소문자 개수만큼 인덱싱해서 처리하는 방법도?
────────────────────────────────────────────────────────────────────────────────
"""