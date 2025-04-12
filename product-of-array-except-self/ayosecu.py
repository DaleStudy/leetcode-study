from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(nums)
        - Space Complexity: O(n)
    """
    def productExceptSelfN(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix, result = [0] * n, [0] * n, [0] * n

        # Calculate prefix and suffix production
        prefix[0], suffix[-1] = nums[0], nums[-1]
        for i in range(1, n - 1):
            prefix[i] = prefix[i - 1] * nums[i]
            j = n - i - 1
            suffix[j] = suffix[j + 1] * nums[j]
        
        # Update the result
        result[0], result[-1] = suffix[1], prefix[-2]
        for i in range(1, n - 1):
            result[i] = prefix[i - 1] * suffix[i + 1]
        
        return result

    """
        - Time Complexity: O(n), n = len(nums)
        - Space Complexity
            - O(1), if output space (result) is ignored
            - O(n), if output space (result) is considered
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        left = 1
        for i in range(n):
            result[i] = left
            left = result[i] * nums[i]
        
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result

tc = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
]

for i, (nums, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.productExceptSelf(nums)
    print(f"TC {i} is Passed!" if e == r else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
