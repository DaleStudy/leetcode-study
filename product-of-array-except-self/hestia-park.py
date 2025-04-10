class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1] * n
        #for left
        for i in range(1,n):
            answer[i]=answer[i-1]*nums[i-1]
        
        tail=1
        #for right 
        for i in range(n-1,-1,-1):
            answer[i] *= tail
            tail *= nums[i]
        return answer



