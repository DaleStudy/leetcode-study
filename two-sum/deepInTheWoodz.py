class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    passed = dict()
    
    for i, num in enumerate(nums):
      other = target - num
      if other in passed:
        return [passed[other], i]
      passed[num] = i
