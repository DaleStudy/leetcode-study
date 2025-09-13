"""
string s가 주어졌을 때, s에서 나올 수 있는 palindrome의 조건을 만족하는 substring 개수를 구하라.
(s는 전부 소문자, 1이상 1000이하)

1. 완전 탐색
- 나올 수 있는 모든 경우의 수 substring을 만들어 palindrome의 조건을 만족하는지 계산

TC: O(N^3)
SC: O(N)

2. 최적화 - 중심 확장
- 모든 palindrome은 어떤 중심을 기준으로 좌우 대칭인 원리를 이용
=> 문자열의 모든 위치를 중심으로 삼고, 양쪽으로 좌우를 확장하며 검사하면 됨
- 중심 개수: 2n - 1

TC: O(N^2)
SC: O(1)

3. 최적화 - DP
    1. 길이 1인 문자열은 항상 팰린드롬
        dp[i][i] = True
    2. 길이 2인 문자열은 두 문자가 같으면 팰린드롬
        s[i] == s[i+1] -> dp[i][i+1] = True
    3. 길이 3 이상인 문자열은 끝 두 문자열이 같고 안에 문자열도 모두 같아야 팰린드롬
        s[i] == s[j] and dp[i+1][j-1] == True -> dp[i][j] = True
        (dp[i+1][j-1] == True시, s[i+1...j-1] 구간의 문자열이 이미 팰린드롬이라는 뜻)

TC: O(N^2)
SC: O(N^2)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # 길이 1 => 항상 팰린드롬
        for i in range(n):
            dp[i][i] = True
            cnt += 1
        
        # 길이 2 => 같은 문자면 팰린드롬
        for i in range(n-1):
            if s[i] == s[i+1]:  # 서로 같은 문자면
                dp[i][i+1] = True  # 팰린드롬
                cnt += 1

        # 길이 3 이상
        for length in range(3, n+1):  # length는 부분 문자열의 길이
            for i in range(n - length + 1):
                j = i + length - 1  # 끝 인덱스
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    cnt += 1

        return cnt


# 25/09/08 복습

"""
“모든 회문은 중심에서 좌우 대칭이다”
→ 따라서 모든 중심점에서 좌우로 확장하면서 회문인지 확인하면
→ 모든 회문 substring을 탐색 가능!

- 중심점의 개수는 총 2n - 1개:
- 홀수 길이: center = 0 ~ n-1 (expand(i, i))
- 짝수 길이: center = 0 ~ n-1 (expand(i, i+1))

TC: O(N^2)
SC: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for center in range(len(s)):
            count += self.expand(s, center, center)

            count += self.expand(s, center, center + 1)
        return count

    def expand(self, s, left, right):
        count = 0
        # 범위를 벗어나지 않고, palindrome이면 확장
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
