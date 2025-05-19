class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1]*len(nums)

        left = 1
        for i in range(len(nums)):
            answer[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= right
            right *= nums[i]

        return answer
