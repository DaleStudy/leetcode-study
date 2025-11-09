# idea: Hash

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
    

'''
Trial and error
Printing I/O inside the loop may cause Output Limit Exceeded
'''

