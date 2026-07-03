# Time: O(N)
# Space: O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        while len(set_nums) > 0 :
            origin_val = set_nums.pop()
            local_len = 1

            val = origin_val - 1
            while val in set_nums:
                local_len += 1
                set_nums.remove(val)
                val -= 1

            val = origin_val + 1
            while val in set_nums:
                local_len += 1
                set_nums.remove(val)
                val += 1
            longest = max(longest, local_len)
        return longest
