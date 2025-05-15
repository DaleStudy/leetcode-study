"""
Constraints:
- 1 <= m, n <= 100

<Solution 1: 조합 활용>

Time Complexity: O(1)
- math.comb() 사용

Space Complexity: O(1)
- 추가 공간 필요없음

풀이 방법:
- 오른쪽 아래 코너로 가는 유니크한 방법의 갯수 찾기
  1. (m-1)번 아래로, (n-1)번 오른쪽으로 가야함 -> 총 (m+n-2)번 이동
  2. 결국 (m+n-2)번의 이동 중 (n-1)번의 오른쪽 이동을 선택하는 조합의 수
  3. Combination 공식 적용: (m+n-2)C(n-1)
    - C(m+n-2, n-1) = (m+n-2)! / ((n-1)! × (m-1)!)
- 풀이가 간결함, 하지만 큰 수에서 오버플로우 가능성 있음
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import comb
        return comb(m+n-2, n-1)

"""
<Solution 2: DP 활용>

Time Complexity: O(m * n)
- m은 row, n은 column의 길이
- 메모이제이션 활용, 모든 좌표에서 재귀 함수의 호출이 딱 한번만 일어나기 때문

Space Complexity: O(m * n)
- 함수의 호출 결과를 저장하는데 격자의 넓이에 비례하는 공간이 필요

풀이방법: 
- 구현이 복잡함, 하지만 큰 수에서도 안정적임
- 재귀와 메모이제이션을 활용한 Top-down DP 접근법
- 현재 위치에서 목적지까지의 경로 수 = 아래로 이동 + 오른쪽으로 이동

2x3 그리드 예시:
각 위치에서 목적지까지 가는 경로 수:
(0,0)=3  (0,1)=2  (0,2)=1
(1,0)=1  (1,1)=1  (1,2)=1

위치 (0,0)에서 시작:
dfs(0,0) = dfs(1,0) + dfs(0,1) = 1 + 2 = 3

경로 3개:
1. 오른쪽, 오른쪽, 아래
2. 오른쪽, 아래, 오른쪽 
3. 아래, 오른쪽, 오른쪽
"""
from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return 1

            total = 0

            if row + 1 < m:
                total += dfs(row + 1, col)

            if col + 1 < n:
                total += dfs(row, col + 1)

            return total

        return dfs(0, 0)
