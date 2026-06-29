# Time: O(n)
# Space: O(2n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = set(nums)
        for j in range(len(nums)-1, -1, -1):
            val = target - nums[j]
            if val in set_nums:
                i = nums.index(val)
                if i != j:
                    return [i, j]

"""
# Time: O(n^2)
# Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


"""
