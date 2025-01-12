# 시간복잡도 : O(n^2)
# 공간복잡도 : O(n)
class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		dp = [False] * (len(s) + 1)
		dp[0] = True

		for i in range(1, len(s) + 1):
			for j in range(i):
				if dp[j] and s[j:i] in wordDict:
					dp[i] = True
					break

		return dp[-1]

