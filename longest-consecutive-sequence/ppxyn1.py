# idea: - 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(list(set(nums))) 
        # sorted_nums = sorted(nums) # duplicate
        max_len = 1
        tmp = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                tmp += 1
            else:
                max_len = max(max_len, tmp)
                tmp = 1 
        ans = max(max_len, tmp)
        return  ans




    