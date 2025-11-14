# Create a empty hash table(seen) and store numbers as a key and their indices as a value
# Iterate through the given array(nums) 
# For each numbers in given array, calculate complement (target - num)
# If complement is in hash table(seen), return array of index of the currnet number and index of complement in hash table(seen)
# If complement is not in has table(seen), store the current number in hash table(seen) and continue checking the numbers
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:      
                return [seen[complement], i]
            seen[num] = i               
        return []
      