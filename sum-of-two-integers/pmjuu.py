'''
시간 복잡도: O(1)
- 덧셈은 비트 연산을 이용하여 수행되며, 정수 크기가 고정되어 있기 때문에 연산 횟수가 제한적입니다.

공간 복잡도: O(1)
- 추가적인 메모리를 거의 사용하지 않습니다.
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32비트 정수 마스크
        MAX_INT = 0x7FFFFFFF  # 32비트 정수의 최대값
        
        while b:
            carry = (a & b) << 1  # 자리 올림 계산
            a = (a ^ b) & MASK  # 덧셈 수행
            b = carry & MASK  # 자리 올림값을 반영하여 다음 연산 진행

        # 음수 처리를 위해 32비트 초과 시 보정
        return a if a <= MAX_INT else ~(a ^ MASK)
