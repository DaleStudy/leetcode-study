"""
    풀이 : 
        비트 연산자 xor, and, shift를 이용해 수행한다
        a는 a와 b의 xor연산 결과
        -> a와 b의 set-bit가 겹치지 않는 위치에서의 합연산을 가능하게 함
        b는 a와 b의 and연산 결과 << 1
        -> a와 b가 둘 다 1인 위치에서 합을 통해 올림수로 올려주는 역할 수행

        파이썬에서는 int가 32비트가 아니므로 1 32개로 이루어진 mask를 설정해주고
        올림수 b가 32비트 범위를 벗어나지 않고 존재할동안 while문 연산을 진행한다
        반복문 진행 후 32비트에 대해서만 return

    TC : O(1)

    SC : O(1)
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while mask & b :
            a, b = a ^ b, (a & b) << 1
        return a & mask if b > 0 else a
