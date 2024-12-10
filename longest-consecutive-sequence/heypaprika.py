# Big-O 예상 : O(nlog(n))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        cur_long = 1
        longest = 1
        for i, num in enumerate(nums):
            if i == 0:
                continue
            else:
                if nums[i-1] + 1 == nums[i]:
                    cur_long += 1
                    if longest < cur_long:
                        longest = cur_long
                else:
                    cur_long = 1
        return longest

