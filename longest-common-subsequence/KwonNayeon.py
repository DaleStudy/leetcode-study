"""
Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

<Solution 1: DFS, 메모이제이션 활용> 

Time Complexity: O(m*n)
- m은 text1의 길이, n은 text2의 길이
- @cache로 중복 계산을 방지하여 각 (i,j) 조합을 한 번만 계산함

Space Complexity: O(m*n)
- 최악의 경우 호출 스택이 두 문자열 길이의 곱만큼 깊어짐

풀이방법:
1. DFS와 메모이제이션을 사용
2. 각 위치 (i,j)에서:
   - 문자가 같으면: 현재 문자를 포함(+1)하고 양쪽 다음으로 이동
   - 다르면: 한쪽만 이동한 경우 중 최댓값 선택
3. base case: 어느 한쪽 문자열 끝에 도달하면 종료
"""
from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
                
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
                
            return max(dfs(i + 1, j), dfs(i, j + 1))
            
        return dfs(0, 0)

"""
<Solution 2: DP>

Time Complexity: O(n * m)
- 2중 for문으로 모든 dp[i][j] 계산

Space Complexity: O(n * m) 
- (n+1) * (m+1) 크기의 DP 테이블 사용

풀이방법:
- 상태 정의: dp[i][j] = text1[:i]와 text2[:j]의 LCS 길이
- Subsequence: 순서만 유지하면 됨
- Substring: 연속적으로 나타나야 함

점화식:
- 문자가 같으면: dp[i][j] = dp[i-1][j-1] + 1
- 문자가 다르면: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

핵심:
- dp 테이블 크기 (n+1) * (m+1): 빈 문자열 케이스 포함
- 최종 답: dp[n][m] (전체 문자열 비교 결과)

노트:
- DP 패턴을 찾아내는 연습하기
- 매트릭스 활용
"""
class Solution:
   def longestCommonSubsequence(self, text1: str, text2: str) -> int:
       n, m = len(text1), len(text2)
       
       # DP 테이블 초기화
       dp = [[0] * (m + 1) for _ in range(n + 1)]
       
       # DP 테이블 채우기
       for i in range(1, n + 1):
           for j in range(1, m + 1):
               if text1[i-1] == text2[j-1]:
                   # 문자가 같으면: 둘 다 선택 + 이전 결과
                   dp[i][j] = 1 + dp[i-1][j-1]
               else:
                   # 문자가 다르면: 둘 중 하나 제외하고 최대값
                   dp[i][j] = max(dp[i-1][j], dp[i][j-1])
       
       return dp[n][m]
