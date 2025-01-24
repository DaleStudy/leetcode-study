# TC:O(n*m), SC:O(1)
# 왼쪽아래로 가는 경로는 왼쪽으로 가는 경로의 경우의 수 + 아래로 가는 경로의 수
# 가장자리로 가는 경로의 경우의 수는 모두 1
# n크기의 리스트 값을 매 번 덮어써서 계산함
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l = [1 for _ in range(n)] 
        for row in range(1, m):
            for col in range(1, n):
                l[col] += l[col - 1]
        
        return l[-1]
