"""
복잡도 : 예상 -> 예상한 이유

시간 복잡도 : O(n) -> 배열의 길이 만큼 반복하므로
공간 복잡도 : O(n) -> n+1 길이의 배열 하나를 생성하므로
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        a = [0] * (len(s)+1)
        a[0] = 1
        a[1] = 1
        for i in range(2, len(s)+1):
            if 1 <= int(s[i-1]) <= 9:
                a[i] += a[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                a[i] += a[i-2]
        return a[-1]

