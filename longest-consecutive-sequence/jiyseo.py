class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0 :
            return 0
        nums = list(set(nums))
        nums.sort()
        ck = nums[0] - 1
        ans = []
        length = 0
        for i in nums :
            if i == ck + 1 :
                length += 1
            else :
                ans.append(length)
                length = 1
            ck = i
        ans.append(length)
        return max(ans)

