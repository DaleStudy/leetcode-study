# 전체 시간복잡도 : O(n^2), 공간복잡도 : O(n)
class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		nums.sort() # 내장함수 sort()의 시간복잡도 O(nlogn)
		result = [] # 공간복잡도 O(n)
		# 시간복잡도 O(n)
		for i in range(len(nums) - 2): 
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			r = len(nums) - 1
			l = i + 1
			# i를 기준으로 l과 r을 탐색하는 시간 복잡도 : O(n)
			while l < r: 
				if nums[i] + nums[l] + nums[r] < 0:
					l += 1
				elif nums[i] + nums[l] + nums[r] > 0:
					r -= 1
				else:
					result.append([nums[i], nums[l], nums[r]])
					while l < r and nums[l] == nums[l + 1]: # 중복 제거 반복문, 이미 진행된 리스트를 다시 탐색하지 않으므로 시간복잡도는 추가되지 않음 
						l += 1
					while l < r and nums[r] == nums[r - 1]:
						r -= 1
					l += 1
					r -= 1
		return result
	
