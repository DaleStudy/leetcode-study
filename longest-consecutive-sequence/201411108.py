# TC: O(n log n), sorted의 시간복잡도, 이후  복잡도는 n
# SC : O(n)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        acc = 1
        max_len = 1

        if len(nums) == 0:
            return 0

        for i, num in enumerate(sorted_nums):
            if i != 0:
                if num == sorted_nums[i - 1]:
                    continue
                if num - 1 == sorted_nums[i - 1]:
                    acc += 1
                    max_len = max(max_len, acc)
                else:
                    acc = 1
        
        return max_len
