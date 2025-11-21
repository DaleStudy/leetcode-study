class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        product1 = [0] * len(nums)
        product2 = [0] * len(nums)

        product1[0] = nums[0]

        for i in range(1, len(nums)):
            product1[i] = product1[i-1]*nums[i]

        product2[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            product2[i] = product2[i+1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                answer.append(product2[1])
            elif i == len(nums)-1:
                answer.append(product1[-2])
            else:
                answer.append(product1[i-1]*product2[i+1])
        return answer
    
