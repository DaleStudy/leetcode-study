class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        res , cnt = 1, 1
        sorted_nums = list(set(nums))
        sorted_nums.sort()
        print(sorted_nums)

        for i in range(len(sorted_nums)-1):
            if sorted_nums[i+1] - sorted_nums[i] == 1:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
        return res
        