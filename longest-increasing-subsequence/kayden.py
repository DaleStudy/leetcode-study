# 시간복잡도: O(N)
# 공간복잡도: O(N)
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        path = []

        for num in nums:
            idx = bisect_left(path, num)
            if len(path) > idx:
                path[idx] = num
            else:
                path.append(num)

        return len(path)