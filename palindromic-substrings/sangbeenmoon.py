class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

        def isPalindrome(start, end) -> bool:

            if end - start == 0:
                return True

            if end - start == 1 :
                return s[start] == s[end]

            if dp[start][end] == 1:
                return True

            if dp[start][end] == -1:
                return False    

            if s[start] == s[end]:
                return isPalindrome(start+1, end-1)    

            return False

        answer = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i,len(s)):
                if isPalindrome(i,j):                    
                    dp[i][j] = 1
                    answer += 1
                else:
                    dp[i][j] = -1

        return answer
                

