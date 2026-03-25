class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0

        res = 0
        length = 1
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] + 1 == nums[i+1]:
                length += 1
            else:
                res = max(res, length)
                length = 1
        
        res = max(res, length)
        return res

        #set을 사용한 풀이
        # if len(nums) <= 0:
        #     return 0
        # res, cnt = 1, 1
        # sorted_nums = list(set(nums))
        # sorted_nums.sort()
        # print(sorted_nums)

        # for i in range(len(sorted_nums) - 1):
        #     if sorted_nums[i + 1] - sorted_nums[i] == 1:
        #         cnt += 1
        #     else:
        #         cnt = 1
        #     res = max(res, cnt)
        # return res
