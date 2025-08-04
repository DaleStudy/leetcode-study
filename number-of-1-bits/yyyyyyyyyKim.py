class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0

        while n > 0:
            answer += n%2   #나머지(현재 비트가 1이면 ++)
            n //= 2         #몫(다음 비트로 이동)
        
        return answer
