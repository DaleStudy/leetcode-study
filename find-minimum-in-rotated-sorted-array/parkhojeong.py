class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = sys.maxsize

        while len(nums) > 0:
            mid_idx = len(nums) // 2

            left = nums[0]
            mid = nums[mid_idx]
            right = nums[-1]

            min_val = min(left, mid, right, min_val)

            if min_val == left:
                break

            if mid < right:
                nums = nums[0: mid_idx]
            else:
                nums = nums[mid_idx + 1:]

        return min_val
