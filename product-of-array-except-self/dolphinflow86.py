# 1) Without using division operator and need to meet linear time complexity, 
# calculate left accumulated product and calculate right accumulated product except iself and then 
# product of left and right to get the result.
# TC: O(N) where N is the length of nums
# SC: O(N) where N is the length of nums
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        acc = 1
        for i in range(1, n):
            acc *= nums[i-1]
            answer[i] = acc
        
        acc = 1
        for i in range(n-2, -1, -1):
            acc *= nums[i+1]
            answer[i] *= acc

        return answer
