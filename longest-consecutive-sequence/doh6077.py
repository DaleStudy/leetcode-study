# 배열을 정렬하고 포인터를 두개 사용
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # sort the given list 
        sorted_nums = sorted(nums)
    
        longest = 1
        curr = 1
        
        l, r = 0, 1
        
        while r < len(sorted_nums):
            # case 1: exactly consecutive (x, x+1)
            if sorted_nums[r] == sorted_nums[l] + 1:
                curr += 1
                longest = max(longest, curr)
                l += 1
                r += 1
            
            # case 2: duplicate (x, x) → ignore, move right pointer
            elif sorted_nums[r] == sorted_nums[l]:
                l += 1
                r += 1
            
            # case 3: gap
            else:
                curr = 1
                l = r
                r += 1
        
        return longest
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums.sort()
        r = 1
        curr = nums[0]
        count = 1
        max_count = 1

        while r < len(nums):
            if nums[r] == curr:
                r += 1
                continue

            if nums[r] == curr + 1:
                count += 1
            else:
                count = 1

            curr = nums[r]
            max_count = max(max_count, count)
            r += 1

        return max_count
