class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n
        isPalindrome = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            isPalindrome[i][i] = True
            if i < n-1 and s[i] == s[i+1]:
                isPalindrome[i][i+1] = True
                count += 1

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if isPalindrome[i+1][j-1] and s[i] == s[j]:
                    isPalindrome[i][j] = True
                    count += 1

        return count