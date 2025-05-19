from typing import List

class Solution:
    """
        - Time Complexity: O(n)
        - Space Complexity: O(1)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")

        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum < num:
                # if current sum is less than current number
                # current sum is replaced with current number
                curr_sum = num
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

tc = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([5,4,-1,7,8], 23)
]

for i, (nums, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.maxSubArray(nums)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
