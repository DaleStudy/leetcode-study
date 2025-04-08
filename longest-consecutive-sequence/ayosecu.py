from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(set_nums) = The number of unique numbers.
        - Space Complexity: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                # Only check for the start number
                cnt = 1
                next_num = num + 1
                while next_num in set_nums:
                    cnt += 1
                    next_num += 1
                longest = max(longest, cnt)
        
        return longest

tc = [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([1,0,1,2], 3)
]

for i, (nums, e) in enumerate(tc, 1):
    sol = Solution()
    result = sol.longestConsecutive(nums)
    print(f"TC {i} is Passed!" if result == e else f"TC {i} is Failed!, Expected: {e}, Result: {result}")
