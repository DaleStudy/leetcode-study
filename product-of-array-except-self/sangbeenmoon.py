# idea
# 1. left[i] = left[0] * left[1] * ... * left[i-1]
# 2. right[i] = right[i+1] * right[i+2] * ... * right[n-1]
# 3. answer[i] = left[i-1] * right[i+1]

# time : O(n)
# space : O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        left[0] = nums[0]
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i]

        right = [1] * len(nums)
        right[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, 0, -1):
            right[i] = right[i+1] * nums[i]
        
        answer = []
        answer.append(right[1])
        for i in range(1, len(nums) - 1):
            answer.append(left[i-1] * right[i+1])
        answer.append(left[len(nums) - 2])
        return answer
