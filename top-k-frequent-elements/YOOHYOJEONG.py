# https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 0
        
        sorted_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        
        return [item[0] for item in sorted_cnt[:k]]