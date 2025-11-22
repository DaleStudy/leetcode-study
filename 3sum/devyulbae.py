"""
Blind 75 - LeetCode Problem 15. 3Sum
https://leetcode.com/problems/3sum/
시간복잡도 O(n^2)
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 중복 원소 스킵

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 중복값 건너뛰기
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1  # 합이 작으니 left를 키워야 함

                else:
                    right -= 1  # 합이 크니 right를 줄여야 함

        return answer

