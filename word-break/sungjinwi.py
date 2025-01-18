"""
    풀이 :
        dp 배열은 s에서 길이n까지의 문자열이 word를 통해 만들어질 수 있는지 여부를 저장
        dp[0]은 빈 문자열이므로 True 나머지는 False로 초기화 (총 길이가 len(s) + 1)
        wordDict를 순회하면서 
            길이 n까지의 문자열이 word로 끝나는지
            n - len(word) 길이가 word로 만들어질 수 있는지 (dp[n - len(word)])

            두 조건 만족하면 dp[n]=True
        dp의 마지막 성분을 return

    
    word의 갯수 W, 문자열 s의 길이 S

    TC : O(S^2 * W)
    각각에 대해 for문 -> S * W
    s에서 word와 비교할 부분문자열 만들 때 -> S

    SC : O(S)
    len(s)만큼 배열 dp를 할당

    유의사항
        - dp의 첫번째 요소
        - if dp[n]일 때 break를 통해 최적화할 것
        - TC구할 때 부분문자열 구하는 복잡도 고려
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for n in range(1, len(s) + 1):
            for word in wordDict:
                if s[n - len(word):n] == word and dp[n - len(word)]:
                    dp[n] = True
                if dp[n]:
                    break
        return dp[-1]
