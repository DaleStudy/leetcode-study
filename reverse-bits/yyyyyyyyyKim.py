class Solution:
    def reverseBits(self, n: int) -> int:
        
        answer = 0 
        
        for i in range(32):
            answer <<= 1   # 왼쪽으로 한 칸 밀어서 자리 확보
            answer |= (n&1) # n의 마지막 비트 추출해서 answer 맨 뒤에 추가
            n >>= 1     # n 오른쪽으로 한 칸 밀기
        
        return answer
