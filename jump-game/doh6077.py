# 55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Recursive 
        # Time: O(max(nums) ^ n)
        # goal = len(nums) - 1

        # def jump_recursive(index):
        #     if index >= goal:
        #         return True
        #     max_jump = nums[index]
        #     if max_jump == 0:
        #         return False
            
        #     while max_jump > 0:
        #         if jump_recursive( index + max_jump):
        #             return True 
        #         else:
        #             max_jump -= 1
        #     return False
        
        # return jump_recursive(0)

        # Greedy - start at end 
        # Time : O(n)

        n = len(nums)
        target = n - 1
        # -1 exclusive 
        for i in range(n-1, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= target:
                target = i 
        return target == 0


# Greedy 
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        
        maxValue = 0 
        reach = len(nums) - 1
        for i in range(0, len(nums)):
            maxValue = max(nums[i] +  i, maxValue)
            if maxValue >= reach: return True
            if maxValue == i and nums[i] == 0:
                return False
            

        return False
