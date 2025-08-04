from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(nums)
        - Space Complexity: O(1)
    """
    def maxProduct(self, nums: List[int]) -> int:
        max_now, max_prod, min_prod = nums[0], nums[0], nums[0]
        
        for num in nums[1:]:
            if num < 0:
                # if number is negative, swap the min/max value
                max_prod, min_prod = min_prod, max_prod          

            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            max_now = max(max_now, max_prod)          
        
        return max_now
    
tc = [
        ([2,3,-2,4], 6),
        ([-2,0,-1], 0)
]

sol = Solution()
for i, (n, e) in enumerate(tc, 1):
    r = sol.maxProduct(n)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
