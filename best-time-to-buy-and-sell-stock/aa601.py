# 시간복잡도 O(n)
# 공간복잡도 O(1)
class Solution:
	def maxProfit(self, prices: list[int]) -> int:
		min_p = prices[0] # 최소 가격 설정  : 배열의 첫 번째 가격
		cur = 0
		max_p = 0
		for n in prices:
			if n < min_p: # 현재 가격이 최소 가격보다 작다면 최소가격 갱신
				min_p = n
			cur = n - min_p # 현재 이익 계산
			if max_p < cur: # 현재 이익과 최대로 얻을 수 있는 이익 비교
				max_p = cur # 최대 이익 갱신신
			
		return max_p
	