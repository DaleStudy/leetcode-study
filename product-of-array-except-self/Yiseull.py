class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]

        # answer[i] -> nums[i] 왼쪽 값들의 곱
        for i in range(1, n):
            answer.append(answer[i - 1] * nums[i - 1])

        tmp = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= tmp
            tmp *= nums[i]

        return answer
