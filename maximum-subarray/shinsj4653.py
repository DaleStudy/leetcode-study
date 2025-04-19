"""
[문제풀이]
# Inputs
- 정수형 nums
# Outputs
- 부분 배열 중 합이 가장 큰 배열의 합
# Constraints
- 1 <= nums.length <= 10^5
- 10^4 <= nums[i] <= 10^4
# Ideas
가장 큰 합을 구하는 방법
정렬은 당연히 X
10^5가 최대라 O(n) 고려 필요
-2 1 -3 4 -1 2 1 -5 4
l, r = 0, 0 -> 움직이면서
 r = 1
-2 < 1 -> -1

-2 -1 -4 0 -1 1 2 -3 1
1. 누적합?

-2 1 -2 4 3 5 6 1 5

5 4 -1 7 8
5 9 8 15 23

지금까지의 합 보다 다음 원소가 크면 그대로 두고, 아니면 합으로 대체
=> TC: O(n), SC: O(1)

[회고]
먼가..때려 맞춘 느낌이라 해설 참고
->
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1] + nums[i]:
                nums[i] += nums[i - 1]

        return max(nums)


