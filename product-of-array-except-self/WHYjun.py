class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            answer[i] = answer[i-1] * nums[i-1]

        for j in range(len(nums)-1, -1, -1):
            if j == len(nums) - 1:
                product = 1
            answer[j] *= product
            product *= nums[j]

        return answer
            
    def productExceptSelfTwoArrays(self, nums: List[int]) -> List[int]:
        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                continue
            leftProduct[i] = leftProduct[i-1] * nums[i-1]

        for j in range(len(nums)-1, -1, -1):
            if j == len(nums) - 1:
                continue
            rightProduct[j] = rightProduct[j+1] * nums[j+1]

        for i in range(len(nums)):
            leftProduct[i] *= rightProduct[i]

        return leftProduct 

