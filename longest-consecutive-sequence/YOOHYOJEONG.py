# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums):
        
        nums_set = set(nums)
        lens = 0

        for n in nums_set:

            if n-1 not in nums_set:
                cur = n
                lenth = 1

                while cur+1 in nums_set:
                    cur += 1
                    lenth += 1
            
                lens = max(lens, lenth)

        return lens
