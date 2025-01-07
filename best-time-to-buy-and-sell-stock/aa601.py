class Solution:
	def maxProfit(self, prices: list[int]) -> int:
		min_p = prices[0]
		cur = 0
		max_p = 0
		for n in prices:
			if n < min_p:
				min_p = n
			cur = n - min_p
			if max_p < cur:
				max_p = cur
			
		return max_p
	
	