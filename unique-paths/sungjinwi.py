"""
    풀이 :
        matrix의 0th row, 0th column을 1로 놓고
        matrix의 각 칸으로 오는 방법을 계산한다
        현재 칸으로 오는 방법은 왼쪽에서 또는 위쪽에서 오는 방법 뿐이므로
        둘을 더한 값이 현재 칸에 오는 방법의 수이다
        전체 matrix가 아닌 row 한 줄 만큼의 배열, cur를 이용하여
        row에 대해 반복문을 돌고 cur의 마지막 요소를 return

    matrix의 크기 m * n

    TC : O(M * N)
        matrix의 모든 요소를 순회하므로

    SC : O(N)
        cur의 크기가 n에 비례하므로
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for _ in range(1, m) :
            for i in range(1, n) :
                cur[i] = cur[i - 1] + cur[i]
        return cur[-1]
