"""
복잡도 : 예상 -> 예상한 이유

시간 복잡도 : O(1) -> 어떤 수가 들어오더라도 상수만큼 연산
공간 복잡도 : O(1) -> 어떤 수가 들어오더라도 상수만큼 할당
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if n % 2 == 1:
                ans += 2**(31-i)
            n = n // 2
        return ans

