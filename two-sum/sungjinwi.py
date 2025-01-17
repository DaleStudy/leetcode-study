"""
	TC : for문 내부 for문
		O(N^2)
	SC : 추가적인 메모리 쓰지 않으므로
		O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums :
            for j in nums :
                if i != j and nums[i] + nums[j] == target :
                    return [i, j]
