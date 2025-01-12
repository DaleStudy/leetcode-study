#시간복잡도 O(N * M)
#공간복잡도 O(N)
class Solution:
	def wordBreak(self, s: str, wordDict: list[str]) -> bool:
		 # 문자열 s의 0번째부터 i번째까지의 문자열이 wordDict의 단어로 분할될 수 있으면 True
		 # 빈 문자열 s[0:0]은 항상 분할이 가능하므로 dp[0] = True
		dp = [False] * (len(s) + 1)
		dp[0] = True
		for i in range(1, len(s) + 1):
			for word in wordDict:
				# 현재 word가 i - len(word)부터 i번째까지의 s의 부분문자열과 일치한다면 True
				# 바로 이전의 지점이 True이고 word만큼의 s 부분문자열이 wordDict 내에 존재한다면 dp[i] = True
				if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
					dp[i] = True
					break
		return dp[-1]
	
