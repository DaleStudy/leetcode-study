class Solution:
    def hammingWeight(self, n: int) -> int:
        num=0
        # Time: O(log n):n의 비트수만큼 Space: O(log n) :stack이 쌓임
        #2로 계속 나누면서 나머지를 세는 방식
        def bin(n):
            nonlocal num
            if n==0: #더 이상 나눌 수 없을때까지
                return
            num+=n%2 
            n//=2
            
            bin(n)
        bin(n)
        return num
