class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        for i in nums :
            if i in dic :
                dic[i] += 1
            else :
                dic[i] = 1
        sorted_dic = sorted(dic.items(), key = lambda x : x[1], reverse = True)
        ans = []
        for i in range(k) :
            ans.append(sorted_dic[i][0])
        
        return ans
        
