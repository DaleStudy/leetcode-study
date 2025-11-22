# idea: dictonary

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        ans = []
        for idx, val in enumerate(nums):
            if val not in count_dict:
                count_dict[val] = 1
            else:
                count_dict[val] +=1
        sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True) #sorted return list / dict.items() is tuple
        # print(sorted_items) 
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans
    
'''
Similar way : Using Counter() function
'''

