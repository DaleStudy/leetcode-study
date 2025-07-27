class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        result = []

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        count = sorted(count.items(), key=lambda x : x[1], reverse=True)
        
        return [item[0] for item in count[:k]]

