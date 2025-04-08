class Solution(object):
    def twoSum(self, nums, target) :
        for i, n in enumerate(nums) :
            if target - n in nums :
                j = nums.index(target - n)
                if i != j :
                    return [i, j]
        return

