# Time: O(N)
# Space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1

        while 0 < i:
            for j in range(1, i+1):
                if nums[i-j] >= j :
                    i -= j
                    break
            else:
                return False
        return True
