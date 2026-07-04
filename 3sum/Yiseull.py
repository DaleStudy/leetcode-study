class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = set()

        nums = sorted(nums)

        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum == 0:
                    answer.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                else:
                    right -= 1

        return list(answer)
