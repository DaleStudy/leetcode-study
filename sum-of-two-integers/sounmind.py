class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32비트 마스크
        MASK = 0xFFFFFFFF
        # 최대 32비트 정수 값
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # a와 b의 XOR (덧셈 결과)
            a_xor_b = (a ^ b) & MASK
            # 자리 올림 (AND 연산 후 한 비트 왼쪽 시프트)
            carry = ((a & b) << 1) & MASK

            # a를 XOR 결과로 업데이트
            a = a_xor_b
            # b를 자리 올림 값으로 업데이트
            b = carry

        if a > MAX_INT:
            # 음수 처리
            a = ~(a ^ MASK)

        return a
