"""
[문제풀이]
# Inputs
숫자로 구성된 문자열 s
# Outputs
decode 가능한 경우의 수
# Constraints
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
# Ideas
모든 경우의 수 -> 1. 우선 완탐

11106 -> 1 1 10 6
가능한 숫자들 : 1~26
11 10 6

진짜 완탐만 가능하지 않나?
1 1 1 0 6 (x)
1 1 1 06 (x)
1 1 10 6 (o)
1 1 106 (x)
11 1 0 6 (x)
10 1 06 (x)

재귀로 구현하면 될듯

n = len(s)
ans = 0

def decode(start_idx):
    global ans
    if start_idx >= n :
        return
for i in range(1, 2):
    num = int(s[start_idx:start_idx + i]
    if i == 1:
        if num != 0:
            ans += 1
            decode(start_idx + 1)
    elif i == 2 :
        if s[start_idx:start_idx+i][0] != 0 and 10 <= num <= 26:
            ans += 1
            decode(start_idx + 1)


2. 완탐 코드 시간 초과
근데 이거 climbing stairs랑 유사한 문제 아닌가?
1과 2로 오를 수 있는 경우의 수 -> 하지만, 숫자 형태 조건이 걸려있어서 씁..

2
2
11
10240

3



[회고]
첫 제출 코드는 시간초과 발생
메모이제이션으로 코드 개선 가능
"""

## 첫 제출 코드
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # ans를 변수로 두고 반환 방식으로 처리
        def decode(start_idx):
            if start_idx >= n:
                return 1  # 끝에 도달하면 1을 반환 (끝까지 도달하면 유효한 디코딩 방법임)

            ans = 0
            for i in range(1, 3):  # 1자리 또는 2자리 숫자를 확인
                if start_idx + i <= n:  # 인덱스 범위 확인
                    num = int(s[start_idx:start_idx + i])
                    if i == 1:
                        if num != 0:  # 1자리 숫자가 0이 아니면 진행
                            ans += decode(start_idx + 1)
                    else:
                        if 10 <= num <= 26:  # 2자리 숫자가 10에서 26 사이일 때 진행
                            ans += decode(start_idx + 2)

            return ans

        return decode(0)  # 0부터 시작

# 두번째 제출 코드

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}
        n = len(s)

        # ans를 변수로 두고 반환 방식으로 처리
        def dfs(start):
            if start in memo:
                return memo[start]

            if s[start] == "0":
                memo[start] = 0
            elif start + 1 < n and int(s[start:start + 2]) < 27:
                memo[start] = dfs(start + 1) + dfs(start + 2)
            else:
                memo[start] = dfs(start + 1)

            return memo[start]

        return dfs(0)  # 0부터 시작

# 해설의 Bottom-up 방식이 이해가 안가 디버깅 시도
class Solution:
    def numDecodings(s):
        dp = [0] * len(s) + [1]
        for start in reversed(range(len(s))):
            if s[start] == "0":
                dp[start] = 0
            elif start + 1 < len(s) and int(s[start : start + 2]) < 27:
                dp[start] = dp[start + 1] + dp[start + 2]
            else:
                dp[start] = dp[start + 1]
        return dp[0]

    numDecodings("2266")


