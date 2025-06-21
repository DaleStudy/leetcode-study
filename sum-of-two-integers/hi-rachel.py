"""
+, - 연산자를 사용하지 않고
정수 a, b의 합을 구해라
"""

# 처음 단순 풀이
class Solution:
    def getSum(self, a: int, b: int) -> int:
        arr = [a, b]
        return sum(arr)
    
"""
비트 연산 풀이

파이썬에서 '&, ^, |, ~, <<, >>' 등의 비트 연산자를 쓰면,
자동으로 이진수로 변환된 값을 기준으로 연산이 수행된다.

carry = (a & b) << 1 = 올림수 계산
& = 같은 자리에서 둘 다 1인 비트만 1
<< 1 올림수는 한자리 위로 이동

a = a ^ b = 덧셈의 합 계산
^는 XOR 연산, 두 비트가 다를 때만 1

(하드웨어 가산기 구현 방법)
def add(a, b):
    while b != 0:  # 더이상 올림수가 없을 때까지
        carry = (a & b) << 1  # 올림수
        a = a ^ b  # 올림수를 제외한 자리 합
        b = carry
    return a

음수 무한 루프 방지를 위해 32 비트 마스크 처리 필요
파이썬에서는 양수 0xFFFFFFFF (32비트 기준 -1) 도 4294967295 라고 나옴.
하지만 C나 Java에선 0xFFFFFFFF는 -1, 32비트 signed 정수 체계로 결과를 해석해야 함.
만약 a > MAX_INT라면, 이건 사실 음수인 값이어야 함

정수 (integer): 그냥 숫자: ..., -2, -1, 0, 1, 2, ...
signed integer (부호 있는 정수): 음수와 양수 둘 다 표현할 수 있는 정수
unsigned integer (부호 없는 정수): 음수는 없고 0과 양수만 표현하는 정수


a & 0xFFFFFFFF -> a의 이진 표현에서 하위 32비트만 남기고, 상위 비트는 모두 0으로 만든다 = 32비트 마스크
~(a ^ MASK) -> 32비트 unsigned를 signed로 바꿈 = 음수 복원

~는 비트를 모두 반전하는 연산
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF   # 32비트 마스크에서 전부 1 (4,294,967,295)
        MAX_INT = 0x7FFFFFFF # 32비트 signed 정수에서 최댓값 (2^31 - 1 = 2,147,483,647)

        while b != 0:
            # 임시 변수에 carry 저장
            carry = (a & b) & MASK  # 32 비트가 넘어가면 상위 비트 잘라버림, 32비트 유지 
            a = (a ^ b) & MASK      # 32비트 유지 
            b = (carry << 1) & MASK # 32비트 유지

        # a가 음수이면 보정
        return a if a <= MAX_INT else ~(a ^ MASK)
