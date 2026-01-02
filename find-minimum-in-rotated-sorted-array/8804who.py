class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while True:
            mid = (left+right)//2
            if nums[left] > nums[right]:
                if nums[left] > nums[mid]:
                    right = mid
                else:
                    left = mid+1
            else:
                return nums[left]
            
