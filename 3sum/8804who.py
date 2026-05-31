class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = {}
        answer = {}
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if -(nums[i]+nums[j]) in temp:
                    ans = str(nums[i])+','+str(nums[j])   
                    answer[ans] = 1
            temp[nums[i]] = 1
        temp_ans = []
        for ans in answer.keys():
            s1, s2 = ans.split(',')
            temp_ans.append([int(s1), int(s2), -(int(s1)+int(s2))])
        return temp_ans
    
