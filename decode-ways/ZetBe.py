'''
문제: 숫자로 이루어진 문자열이 주어졌을 때, 이를 알파벳으로 디코딩하는 방법의 수를 구하는 문제(여기서 1은 'A', 2는 'B', ..., 26은 'Z'에 해당).
풀이: 동적 계획법을 사용하여 각 위치까지의 디코딩 방법의 수를 계산
    1. dp[i]를 문자열의 i번째 문자까지 디코딩하는 방법의 수라고 정의
    2. 문자열의 i번째 문자가 '0'인 경우, 이전 문자가 '1' 또는 '2'인 경우에만 유효한 디코딩이 가능하므로 dp[i] = dp[i-2]
    3. 문자열의 i번째 문자와 이전 문자를 합쳐서 10~26 사이의 숫자가 되는 경우, dp[i] = dp[i-1] + dp[i-2]
    4. 그 외의 경우에는 dp[i] = dp[i-1]
시간복잡도: O(n)
    문자열을 한 번 순회하며 dp 배열을 채우므로 전체 시간복잡도는 O(n)이다.
공간복잡도: O(n)
    dp 배열을 사용하므로 전체 공간복잡도는 O(n)이다.
사용한 자료구조: 리스트
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        string = list(s)
        n = len(string)        
        dp = [0 for i in range(n)]
        if string[0] == '0':
            return 0
        if n == 1:
            return 1
        if n == 2:
            if 11 <= int(s) <= 19 or 21 <= int(s) <= 26:
                return 2
            elif int(s) == 10 or int(s) == 20:
                return 1
            elif '0' in string:
                return 0
            else:
                return 1
        dp[0] = 1
        if string[1] == '0' and 3 <= int(string[0]):
                return 0
        if 11 <= int(string[0])*10 + int(string[1]) <= 19 or 21 <= int(string[0])*10 + int(string[1]) <= 26:
            dp[1] = 2
        else:
            dp[1] = 1

        for i in range(2, n):
            if string[i] == '0' and (3 <= int(string[i-1]) or int(string[i-1]) == 0):
                return 0
            if 11 <= int(string[i-1])*10 + int(string[i]) <= 19 or 21 <= int(string[i-1])*10 + int(string[i]) <= 26:
                dp[i] =  dp[i-2] + dp[i-1]
            elif int(string[i-1])*10 + int(string[i]) == 10 or int(string[i-1])*10 + int(string[i]) == 20:
                dp[i] = dp[i-2]
            else:
                dp[i] += dp[i-1]
        
        return dp[n-1]
    

'''
너무 복잡하게 풀었기 때문에 ai에게 간결한 풀이를 알려달라해서 공유드립니다

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # dp[i] : s의 앞 i글자를 해석하는 방법의 수
        dp = [0] * (n + 1)
        
        # 초기값 설정 (빈 문자열은 1가지 방법, 첫 글자는 위에서 0체크 했으므로 1가지)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # 1. 한 자리 숫자 해석 (1~9)
            # 현재 숫자(s[i-1])가 '0'이 아니면, 이전 상태(dp[i-1])를 계승
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # 2. 두 자리 숫자 해석 (10~26)
            # 이전 숫자와 현재 숫자를 합쳐서 10~26 사이라면, 전전 상태(dp[i-2])를 더함
            two_digit = int(s[i-2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]
'''

