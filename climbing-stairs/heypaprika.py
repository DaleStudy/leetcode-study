"""
복잡도 : 예상 -> 예상한 이유

시간 복잡도 : O(n) -> 배열의 길이 n-2 만큼 반복하므로
공간 복잡도 : O(n) -> n 길이의 배열 하나를 생성하므로
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        a = [0] * n
        a[0] = 1
        a[1] = 2
        for i in range(2, n):
            a[i] = a[i-1] + a[i-2]
        return a[n-1]

