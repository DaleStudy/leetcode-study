"""
Inputs:
정렬되지 않은 정수 배열 nums

Outputs:
가장 긴 연속된 부분 배열의 길이

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

Time Complexity: O(n) 이어야함
어차피 n 최대 길이가 10^5이라 O(n^2)은 불가능!

1 2 3 4라면,
2 3 4
3 4  -> 이 두 후보는 정답에 포함됨

Space Complexity: O(n)
중복 제거한 nums 인 numSet의 크기는 최대 n
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ret = 0

        for num in numSet:
            if num - 1 in numSet:
                continue

            cnt = 1

            while num + 1 in numSet:
                cnt += 1
                num += 1

            ret = max(ret, cnt)

        return ret
