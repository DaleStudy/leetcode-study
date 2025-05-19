# 디코드 가능 1 ~ 26
# 숫자의 첫 번째 자리가 0이라면 decode x
# O(n) time, O(n) space

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1} # 문자열 끝에 도달했을 때는 경우의 수 1

        def dfs(start):
            if start in memo: # 이미 계산한 위치 재계산 x
                return memo[start]
            if s[start] == "0":
                memo[start] = 0
            elif start + 1 < len(s) and int(s[start:start + 2]) < 27: # 두 자리로 해석 가능할 때
                memo[start] = dfs(start + 1) + dfs(start + 2) # 첫 한 자리만 decode 경우 + 두 자리 한꺼번에 decode 경우
            else:
                memo[start] = dfs(start + 1) # 두 자리로 decode 불가능할 때 -> 한 자리만 decode
            return memo[start]
        return dfs(0)
