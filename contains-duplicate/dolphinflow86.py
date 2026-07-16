# First approach: using a set to check for duplicates while iterating through nums
# TC: O(n), where n is the number of elements in nums 
# SC: O(n), where n is the number of elements in nums
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            # check if the number exists in the set during each iteration
            if num in seen:
                return True
            seen.add(num)
            
        return False


# Second approach: brute-force method using nested for loops to check every pair for duplicates.
# Inefficient time complexity (quadratic time) but has a constant space complexity.
# TC: O(n^2), where n is the number of elements in nums 
# SC: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False


# Third approach: to decrease time complexity from the brute-force approach, by sorting the array and comparing adjacent elements
# TC: O(n log n), where n is the number of elements in nums
# SC: O(n), where n is the number of elements in nums. Initially I thought Python's sorting algorithm was the same as C++'s IntroSort. 
# However, Python uses Timsort uses which requires O(n) space in the worst case
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        # Compare adjacent elements
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
                
        return False
