class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # 1. 왼쪽 곱 저장
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # 2. 오른쪽 곱을 곱해주기
        right_product = 1
        for i in reversed(range(n)):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
