"""
시간복잡도: O(1)  # 32번만 반복하므로 항상 상수 시간 복잡도임
공간복잡도: O(1)

1. ans를 0으로 초기화한다.
3. ans를 왼쪽으로 1비트 시프트한 후, n의 마지막 비트를 OR 연산한다.
4. n을 오른쪽으로 1비트 시프트한다.
- 3, 4 과정을 32번 반복한다.
5. ans를 반환한다.
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for _ in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1

        return ans
