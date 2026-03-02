class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i,n in enumerate(nums):
            t = target - n
            if t in nums[i+1:]:
                answer = [i, (i+1) +nums[i+1:].index(t)]
                return answers