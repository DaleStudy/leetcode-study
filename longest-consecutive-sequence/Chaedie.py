"""
Solution: 
    0. i will use prev, cur pointers in for loop, 
        so i have to get rid of edge case when len of nums is at most 1
    1. use hash set for remove duplicate elements 
    2. sort list
    3. iterate sorted_nums and use two pointers (prev, cur) 
        compare prev and cur and count if the difference is 1
    4. use max method, memorize maxCount
    5. return maxCount

Time Complexity: 
    1. remove duplicate by hash set -> O(n)
    2. sort the list -> O(n log n)
    3. iterate sorted_nums -> O(n)

    so time complexity of this solution will be O(n log n)

Space Complexity:
    1. set() -> O(n)
    2. sorted_nums -> O(n)
    3. count , maxCount -> O(1)

    space complexity of this solution will be O(n)
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        sorted_nums = sorted(list(set(nums)))

        count = 1
        maxCount = 1
        for i in range(1, len(sorted_nums)):
            prev = sorted_nums[i - 1]
            cur = sorted_nums[i]
            if prev + 1 == cur:
                count += 1
                maxCount = max(count, maxCount)
            else:
                count = 1

        return maxCount
