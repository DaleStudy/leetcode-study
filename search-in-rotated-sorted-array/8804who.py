class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start+(end-start)//2

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid+1
                else:
                    end = mid-1
        return -1
    
