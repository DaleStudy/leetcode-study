# https://leetcode.com/problems/maximum-subarray/

# 이전까지 누적한 값이 음수면 버리고 현재 값부터 다시 시작
# 한 번만 순회 -> O(n)

class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
