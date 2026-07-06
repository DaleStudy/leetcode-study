class Solution:

    def __init__(self):
        self.memo = dict()

    def climbStairs(self, n: int) -> int:
        
        # 공간복잡도 : n의 개수 만큼 memo가 할당되므로 o(n)
        # 시간복잡도 : 각 칸에 대해서 계산이 1번씩만 되므로 o(n)

        # base 
        if n <= 2 : 
            return n
        
        # 이미 계산 한 값이라면 반환
        if n in self.memo:
            return self.memo[n]

        # 1칸 전과 2칸 전의 결과를 합한 것을 반환.
        result = self.climbStairs(n-2) + self.climbStairs(n-1)
        self.memo[n] = result

        return result
