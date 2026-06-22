# 7기 풀이
# 시간 복잡도: O(1)
# - 숫자가 32비트이기 때문에 최대 32번의 루프
# 공간 복잡도: O(1)
# - 몇 개의 변수만
class Solution:
    # 해당 문제는 bit 연산을 이용해서 덧셈을 구현
    def getSum(self, a: int, b: int) -> int:
        # 문제 조건에 두 숫자는 모두 32bit 숫자임을 명시되었으며
        # 이 mask를 사용해야 음수 대응도 가능해진다.
        mask = 0xFFFFFFFF

        while b & mask:
            carry = (a & b) << 1  # 올림 표현
            a = a ^ b  # XOR 연산, 비트의 덧셈은 XOR과 동일하기 때문
            b = carry  # 올림한 것을 다음 연산에 사용한다

        # b가 0이 아니라면 무한 비트로 올라가고 있음을 의미하며
        # 음수 대응을 위해 a와 mask를 and 연산하여 return
        return a if b == 0 else a & mask
