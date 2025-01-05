# space complexity: O(n^2)
# time complexity: O(n^2) (*exactly, n^2 / 2)
class Solution:
	def countSubstrings(self, s: str) -> int:
		dp = [[False] * len(s) for _ in range(len(s))] # dp[i][j] = True if s[i:j+1] is a palindrome
		for i in range(len(s)):
			for j in range(i, -1, -1):
				if i == j:
					dp[j][i] = True
					continue
				if i - j == 1:
					dp[j][i] = s[i] == s[j]
					continue
				if s[i] == s[j]:
						if dp[j+1][i-1]:
							dp[j][i] = True
		
		return sum([sum(row) for row in dp])

