from typing import List

class Solution:
    """
        - Time Complexity: O(logn), n = len(nums)
        - Space Complexity: O(1)
    """
    def findMin(self, nums: List[int]) -> int:
        # Binary Search
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2            
            if nums[mid] > nums[r]:
                # if min number located in right side
                l = mid + 1
            else:
                # if min number located in left side (including current pivot)
                r = mid
        
        return nums[l]

tc = [
        ([3,4,5,1,2], 1),
        ([4,5,6,7,0,1,2], 0),
        ([11,13,15,17], 11)
]

for i, (nums, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.findMin(nums)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
