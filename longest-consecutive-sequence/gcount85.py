"""
# Intuition
Sort array first, then compare every element with its previous one
while counting consecutive ones.

# Approach
1. sort
2. initiate variables: max_count, current_count, previous_element_idx
3. for n in nums:
    3-1. if n is nums[prev] + 1: current_count++
        elif n is smaller or bigger than nums[prev] + 1:
            update max_count and initiate current_count
    3-2. increase previous element index
4. return max_count

# Complexity
- Time complexity: O(N log N)

- Space complexity: O(N)
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()  # Time complexity O(N log N), Space complexity O(N)
        max_count = 0
        count = 1
        prev = 0
        for n in nums[1:]:  # Space complexity O(N)
            if n == nums[prev] + 1:
                count += 1
            elif n < nums[prev] or n > nums[prev] + 1:
                max_count = max(count, max_count)
                count = 1
            prev += 1
        return max(count, max_count) if len(nums) else 0
