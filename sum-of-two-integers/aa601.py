'''
TC : O(1)
    최대 32번 반복
SC : O(1)
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32비트 정수 연산을 위한 마스크 비트 설정
        mask = 0xFFFFFFFF
        while b & mask :
            tmp = a
            a = a ^ b
            b = (tmp & b) << 1
        if b > 0: # 연산결과 32비트를 벗어난 경우 a의 32비트까지 반환
            return a & mask
        else: # 32비트 안에서 연산이 끝났다면 마스크할 필요 없음
            return a
