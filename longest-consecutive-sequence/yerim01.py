# Leetcode 128: https://leetcode.com/problems/longest-consecutive-sequence/
# Goal: Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.
# Constraints:
# - Unsorted array
# - Must run in O(n) time
# - Duplicates exist
# Approach:
# - Use a variable `longest=0` to track the length of the longest sequence.
# - Convert nums into a hash set to check numbers in O(1).
# - Iterate the nums.
# - Use variables `currentL=1` to track the length of current sequence
#   and `j=1` to represent the distance from the current number.
# - For checking larger numbers, do current num + j
#   and for checking smaller numbers, do current num - j
# - Iterate through the set while consecutive number exists in the set.
#   If it founds the number, remove it from the set and update currentL & j.
# - Update longest with the mximum length.
# - Return longest.
# Time complexity: O(n)
# - Each number is removed from the set
# Space complexity: O(n)
# - Using a set. n -> size of the nums
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)

        for c in nums:
            currentL = 1
            j = 1

            while c+j in s:
                s.remove(c+j)
                currentL += 1
                j += 1

            j = 1
            while c-j in s:
                s.remove(c-j)
                currentL += 1
                j += 1
            
            longest = max(longest, currentL)
        
        return longest
