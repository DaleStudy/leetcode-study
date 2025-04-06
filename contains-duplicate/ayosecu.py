from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(nums)
        - Space Complexity: O(N)
            - N = len(set_check) = The number of unique numbers
            - If there is no duplicated numbers, N = n
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_check = set()

        for num in nums:
            if num in set_check:
                return True
            else:
                set_check.add(num)
        
        return False

tc = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1,1,1,3,3,4,3,2,4,2], True)
    ]

for i, (t, e) in enumerate(tc, 1):
    sol = Solution()
    result = sol.containsDuplicate(t)
    print(f"TC {i} is Passed!" if result == e else f"TC {i} is Failed! - Expected: {e}, Result: {result}")
