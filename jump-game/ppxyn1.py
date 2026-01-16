# idea: recursive
# Time Complexity : O(n^n) w.o cache
#                 : O(n^2)   w cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) -1

        @cache
        def jump(i):
            if i == last_idx:
                return True
            # jump from 1 to numbers                 
            for j in range(1, nums[i] + 1):
                if jump(i + j):
                    return True

            return False
        return jump(0)



