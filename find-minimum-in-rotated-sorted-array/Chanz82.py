class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[right] < nums[mid]: # right 와 mid 사이에 최소 값이 존재
                left = mid + 1
            else:
                right = mid
            
        return nums[left]
