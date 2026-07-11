class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        # left -> right
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1] # 왼쪽에 있는 것들을 곱하자

        # right -> left
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * right_product
            right_product = right_product * nums[i]


        return answer
