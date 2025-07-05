"""
[문제풀이]
# Inputs
n: int
# Outputs

ans: arr
길이: n + 1

ans내 각 원소들 : ans[i]: i의 이진법에서 1의 개수

# Constraints
0 <= n <= 10^5

# Ideas
2중 for문 이면 안됨

[회고]
dp를 활용한 풀이도 같이 알아두자
"""

# 내 풀이
class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = []

        for i in range(n + 1):
            if i == 0 or i == 1:
                ans.append(i)
                continue

            num = i
            cnt = 0
            while num > 0:
                num, n = num // 2, num % 2
                if n == 1:
                    cnt += 1

            ans.append(cnt)

        return ans

# 해설
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for num in range(1, n + 1):
            dp[num] = dp[num // 2] + (num % 2)
        return dp


