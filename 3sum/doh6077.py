from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n - 2):
            # i 중복 스킵
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # nums[i] 이후는 전부 양수 → 더 이상 0 못 만듦
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # left 중복 스킵
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # right 중복 스킵
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
