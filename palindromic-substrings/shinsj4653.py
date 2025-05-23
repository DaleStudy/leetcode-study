"""
[문제풀이]
# Inputs
string  s

# Outputs
the number of palindromic substrings

# Constraints
1 <= s.length <= 1000
s consists of lowercase English letters.

# Ideas
부분 문자열 중 팰린드롬 인거
순열?
10^3 => 시초 예상

코드를 짜보니 O(n^3) 나오긴하는데 우선 정답

[회고]

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0

        for num in range(1, len(s) + 1):
            for i in range(len(s) - num + 1):
                ss = s[i:i + num]
                if ss == ss[::-1]:
                    ret += 1

        return ret

# 해설보고 스스로 풀이

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}

        for start in range(len(s)):
            for end in range(start, -1, -1):
                if start == end:
                    dp[(start, end)] = True

                elif start + 1 == end:
                    dp[(start, end)] = s[start] == s[end]

                else:
                    dp[(start, end)] = dp[(start + 1, end - 1)] and s[start] == s[end]

        return dp.values().count(True)

# 기존 값 재활용하려면 end 부터 세야하는게 이해가 안감
# -> 다시 풀이
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}

        for end in range(len(s)):
            for start in range(end, -1, -1):
                if start == end:
                    dp[(start, end)] = True

                elif start + 1 == end:
                    dp[(start, end)] = s[start] == s[end]

                else:
                    dp[(start, end)] = dp[(start + 1, end - 1)] and s[start] == s[end]

        return list(dp.values()).count(True)

