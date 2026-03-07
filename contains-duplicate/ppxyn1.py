# idea: Hash

# Ans 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dict={}
        for i in range(len(nums)):
            # print(count_dict) 
            if nums[i] in count_dict.keys():
                return True
            else:
                 count_dict[nums[i]] = 1
        return False
    

# Ans 2
# Time Complexity: O(n) (Set)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


