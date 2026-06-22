# idea: For each number n in nums, check if (target - n) exists in the remaining elements.

# Ans 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            required_num = target - num
            if required_num in nums[idx+1:]:
                return [idx, nums.index(required_num, idx+1)]



# Ans 2
# idea : Two-pointer
# Time Complexity : O(n log n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Keep original indices !
        new_nums = [(idx, num) for idx, num in enumerate(nums)]
        new_nums.sort(key=lambda x: x[1])

        left, right = 0, len(new_nums)-1
        
        while left < right:
            idx_left, idx_right = new_nums[left][0], new_nums[right][0]
            val = new_nums[left][1] + new_nums[right][1]
            if val == target:
                return [idx_left, idx_right]
            elif val < target:
                left +=1 
            else:
                right -=1
        return []


