"""
Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

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
