class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

        ## TC: O(n), SC: O(1)

        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1

        ## TC: O(n), this may fater than bintree way if gvien nums are longer
        ## SC: O(n)
