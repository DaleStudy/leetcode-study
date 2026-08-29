# 오래전 배운 2진수 구하는 방법을 그대로 적용.
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            remainder = n % 2
            if remainder == 1:
                cnt += 1
            n = n // 2
        return cnt
    
# LLM 이 알려준 다른 풀이.
# 그렇지만 라이브코딩테스트 등에서는 썩 적합하지 않은듯.
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# 또 다른 풀이. 비트연산 활용.
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1   # 맨 오른쪽 비트가 1인지 확인
            n >>= 1           # 오른쪽으로 한 칸 시프트
        return count
