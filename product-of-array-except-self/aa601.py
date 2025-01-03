#시간복잡도: O(n), 공간복잡도 : O(n)

class Solution:
	def productExceptSelf(self, nums: list[int]) -> list[int] :
		a = [1] * len(nums)
		for n in range(len(nums) - 1) :
			a[n + 1] = a[n] * nums[n]

		b = [1] * len(nums)
		for n in range(len(nums) - 1, 0, -1) :
			b[n - 1] = b[n] * nums[n]

		c = [1] * len(nums)
		for n in range(len(nums)) :
			c[n] = a[n] * b[n]
		return c

