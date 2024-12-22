"""
Solution1:
    sliding window 일 것 같지만 구현이 어려워 일단 Brute Force 부터 진행합니다.
    -> 시간 초과로 실패

Time: O(n^2) =  n(for) * n(for)
Space: O(n) = cur 배열
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float(-inf)
        for i in range(n):
            cur = []
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                cur.append(nums[j])
                max_sum = max(max_sum, cur_sum)
        return max_sum


"""
Solution2:
    Sliding Window로 풀 수 있을거라 생각했는데 잘 안되었습니다.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float(-inf)

        l = 0
        window = 0
        for r in range(n):
            window += nums[r]
            max_sum = max(max_sum, window)
            while max_sum < window:
                l += 1

        return max_sum


"""
Solution3 - 알고달레: 
    솔루션을 통해 학습했습니다.
    이해가 어려워 다시 풀어볼 예정입니다.

Time: O(n)
Space: O(1)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(cur_sum, max_sum)
        return max_sum
