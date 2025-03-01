# Time Complexity: O(n) - go through the array once, checking jump reachability.
# Space Complexity: O(1) - no extra space used, just a few variables.

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            # if there's only one element, we're already at the last index
            return True  

        # start from second-to-last index
        backtrack_index = len(nums) - 2 
        # need to jump at least once to reach the last index 
        jump = 1  

        while backtrack_index > 0:
            # If we can jump from this position to the next "safe" spot
            if nums[backtrack_index] >= jump:
                # reset jump counter since we found a new reachable point
                jump = 1  
            else:
                # otherwise, increase the jump required
                jump += 1  

            # move one step left
            backtrack_index -= 1  

        # finally, check if we can reach the last index from the starting position
        return jump <= nums[0]
