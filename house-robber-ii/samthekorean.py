# TC : O(n), where n is the number of houses.
# SC : O(1)
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0], max(nums[1], nums[2]))

        a = nums[0]
        b = max(nums[0], nums[1])
        c = -1
        a1 = nums[1]
        b1 = max(nums[1], nums[2])
        c1 = -1

        for i in range(2, n):
            if i < n - 1:
                c = max(nums[i] + a, b)
                a = b
                b = c
            if i > 2:
                c1 = max(nums[i] + a1, b1)
                a1 = b1
                b1 = c1

        return max(c, c1)
