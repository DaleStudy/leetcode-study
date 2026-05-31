'''
문제: 주어진 문자열이 사전에 있는 단어들로 구성될 수 있는지 여부를 판단하는 코드를 작성하시오.
풀이: 동적 프로그래밍(DP)을 사용하여 문자열의 각 위치까지 사전에 있는 단어들로 구성될 수 있는지 여부를 기록합니다.
시간복잡도: O(n*m) (n은 문자열 s의 길이, m은 단어 사전의 단어 수)
공간복잡도: O(n)
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s))]
        for i in wordDict:
            if i == s[:len(i)]:
                dp[len(i)-1] = True
        
        for i in range(1, len(s)):
            if dp[i-1] == True:
                
                for j in wordDict:
                    if i+len(j) <= len(s) and j == s[i:i+len(j)]:
                        dp[i+len(j)-1] = True
        return dp[len(s)-1]

