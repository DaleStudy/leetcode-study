"""
	TC : for문 두번 반복하므로 O(2N)
		-> O(N)
	SC : answer 배열 외에 추가적인 메모리는 factor 변수 하나이므로
		-> O(1)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        factor = 1
        for i in range(len(nums) - 1) :
            factor *= nums[i]
            answer[i + 1] *= factor
        factor = 1
        for i in range(len(nums) - 1, 0, -1) :
            factor *= nums[i]
            answer[i - 1] *= factor
        return answer
