"""
    풀이 :
        부분문자열 중에 가장 많은 빈도의 문자를 기준으로 다른 문자가 k개 이하로 있으면
        같은 반복문자열로 만들 수 있다
        sliding window 기법을 통해 최다빈도 문자와 다른 문자가 k개 초과이면 start를 이동시킨다

    SC : O(N)
        start, end포인터는 문자열 길이에 비례해 반복해서 이동하므로 (max 연산은 O(26))

    TC : O(1)
        counter 딕셔너리는 최대 알파벳 개수만큼의 메모리를 차지하므로 O(26)으로 상수이다다
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        counter = {}
        max_len = 0
        while end < len(s) :
            counter[s[end]] = counter.get(s[end], 0) + 1
            while end - start + 1 - max(counter.values()) > k :
                counter[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len
