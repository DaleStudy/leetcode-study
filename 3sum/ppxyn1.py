# idea: sorting + two pointer
# The idea was straightforward, but remove the duplication logic was the tricky.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            if i > 0 and  nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return answer


