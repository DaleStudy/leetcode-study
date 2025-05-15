"""
Constraints:
- 1 <= m, n <= 100

<Solution 1>

Time Complexity: O(1)
- math.comb() 사용

Space Complexity: O(1)
- 추가 공간 필요없음

풀이 방법:
- 오른쪽 아래 코너로 가는 유니크한 방법의 갯수 찾기
  1. (m-1)번 아래로, (n-1)번 오른쪽으로 가야함 -> 총 (m+n-2)번 이동
  2. 결국 (m+n-2)번의 이동 중 (n-1)번의 오른쪽 이동을 선택하는 조합의 수
  3. Combination 공식 적용: (m+n-2)C(n-1)

Further Consideration:
- DP로 풀어보기
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import comb
        return comb(m+n-2, n-1)

"""
<Solution 2>

Time Complexity: 
- 

Space Complexity: 
- 

풀이방법: 
"""

