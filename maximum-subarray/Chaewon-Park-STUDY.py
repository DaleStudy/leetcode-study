class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        k=len(nums)
        # Time: O(n) - 배열 loop, Space: O(1) 
        prev=nums[0] #이전까지의 합 중 max
        max_val=prev #전체 중에서 최대 
        for i in range(1,k):
            if nums[i]>=prev+nums[i]:  #이전합이 0이하인 경우 리셋
                prev=nums[i]
            else:
                prev+=nums[i]
            max_val = max(max_val, prev)
        return max_val
        
