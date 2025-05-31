class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 비트 연산(보완이 필요함, python은 무제한정수를 사용하므로 mask써서 32bit 정수로 잘라줘야함)
        mask = 0xFFFFFFFF       # 32비트 정수 마스크
        max_int = 0X7FFFFFFF    # 양수 최대값
        
        while b != 0:
            # 자리올림(AND연산)
            carry = (a&b) & mask
            # 자리올림없이 더하기(XOR연산)
            a = (a^b) & mask
            # 왼쪽으로 1 비트이동(다음 자리에서 더할 carry값)
            b = (carry << 1) & mask

        # a가 음수인 경우 보수 변환
        return a if a <= max_int else ~(a^mask)

        # return sum([a,b])
