from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(nums)
        - Space Complexity: O(N)
            - N = len(dic) = The number of unique numbers
            - Worst case, it would be n. => O(N) => O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Save "num:index" key-value to a dictionary
        dic = {}
       
        for i, num in enumerate(nums):
            # Check diff value is already in a dictionary
            diff = target - num
            if diff in dic:
                # If there is a diff value, return indices of pair
                return [dic[diff], i]
            dic[num] = i

        return []

tc = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]

for i, (nums, target, e) in enumerate(tc, 1):
    sol = Solution()
    result = sol.twoSum(nums, target)
    result.sort()
    print(f"TC {i} is Passed!" if result == e else f"TC {i} is Failed! - Expected: {e}, Result: {result}")
