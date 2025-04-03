from typing import List
from collections import Counter

class Solution:
    """
        - Time Complexity: O(nlogk), n = len(nums)
            - Counter(nums) => O(n)
            - Counter.most_common(k) => O(nlogk)
            - O(n) + O(nlogk) => O(nlogk)
        - Space Complexity: O(N)
            - N = len(counter_nums) = The number of unique numbers
            - Worst case => No duplicated numbers => N = n
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [key for (key, val) in c.most_common(k)]

tc = [
        ([1,1,1,2,2,3], 2, [1, 2]),
        ([1], 1, [1])
]

for i, (nums, k, e) in enumerate(tc, 1):
    sol = Solution()
    result = sol.topKFrequent(nums, k)
    result.sort()
    print(f"TC {i} is Passed!" if result == e else f"TC {i} is Failed! - Expected: {e}, Result: {result}")
