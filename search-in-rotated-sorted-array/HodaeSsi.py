from typing import List

# 시간 복잡도 : O(log n) (* 최대 세번의 이진 탐색 수행)
# 공간 복잡도 : O(1)
class Solution:
	def find_pivot_idx(self, src_list: List[int], start_idx: int, end_idx: int) -> int:
		if start_idx == end_idx:
			return start_idx
		mid_idx = (start_idx + end_idx) // 2
		if src_list[mid_idx] > src_list[end_idx]:
			return self.find_pivot_idx(src_list, mid_idx + 1, end_idx)
		else:
			return self.find_pivot_idx(src_list, start_idx, mid_idx)
		

	def find_target_idx(self, src_list: List[int], start_idx: int, end_idx: int, target) -> int:
		if start_idx > end_idx:
			return -1
		if start_idx == end_idx:
			if src_list[start_idx] == target:
				return start_idx
			else:
				return -1

		mid_idx = (start_idx + end_idx) // 2
		if src_list[mid_idx] == target:
			return mid_idx
		elif src_list[mid_idx] > target:
			return self.find_target_idx(src_list, start_idx, mid_idx - 1, target)
		else:
			return self.find_target_idx(src_list, mid_idx + 1, end_idx, target)
			

	def search(self, nums: List[int], target: int) -> int:
		if nums[0] > nums[len(nums) - 1]:
			pivot_idx = self.find_pivot_idx(nums, 0, len(nums) - 1)
			left = self.find_target_idx(nums, 0, pivot_idx - 1, target)
			if left != -1:
				return left
			else:
				return self.find_target_idx(nums, pivot_idx, len(nums) - 1, target)
		else:
			return self.find_target_idx(nums, 0, len(nums) - 1, target)

