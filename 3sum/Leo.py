class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i, ch in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = ch + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([ch, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res

        ## TC: O(n^2), SC: O(1)
