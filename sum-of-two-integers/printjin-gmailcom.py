# recheck needs to be done

class Solution:
    def getSum(self, a, b):
        MASK = 0xFFFFFFFF  # 32비트 정수를 흉내 내기 위한 마스크 (십진수로는 4294967295)
        MAX_INT = 0x7FFFFFFF  # 32비트에서의 양수 최댓값 (2147483647)

        while b != 0:
            # a ^ b: 자리올림(carry) 없이 더한 값
            # a & b: 같은 자리에 1이 있으면 자리올림이 생긴다는 의미
            # (a & b) << 1: 자리올림을 왼쪽으로 이동하여 실제 올림 연산 위치로 맞춤
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # 최종적으로 a에 정답이 들어감
        # 그런데 32비트 부호있는 정수에서는 양수 최대값이 MAX_INT
        # a > MAX_INT라면 음수라는 뜻이므로, 보수 처리를 해줌
        return a if a <= MAX_INT else ~(a ^ MASK)
