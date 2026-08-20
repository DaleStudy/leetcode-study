"""
시간복잡도: O(1)
공간복잡도: O(1)

16비트 정수 범위에서 각 비트를 하나씩 확인하며 덧셈을 수행한다.

각 비트의 합은 XOR 연산으로 구하고,
올림수(carry)는 두 비트 이상이 1인 경우를 OR 연산으로 계산한다.
  - 전가산기 원리 적용

계산된 각 비트는 ans의 해당 위치에 저장한다.

Python의 int는 고정된 비트 폭을 가지지 않으므로,
최종 결과의 최상위 비트가 1인 경우에는 16비트 음수로 직접 변환한다.

MASK와 XOR하여 16비트 범위 안에서 비트를 반전한 뒤,
~ 연산을 적용하여 Python의 음수 정수 형태로 변환한다.
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFF
        CHECK = 0x8000

        ans = carry = 0
        for i in range(16):
            a_bit = a & 1
            b_bit = b & 1

            left = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (b_bit & carry) | (a_bit & carry)

            ans |= left * 2**i
            a >>= 1
            b >>= 1

        if ans & CHECK == 0:
            return ans
        else:
            return ~(MASK ^ ans)
