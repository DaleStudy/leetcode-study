class Solution(object):
    def topKFrequent(self, nums, k):
        unique_no = set(nums)
        data = []

        for i in unique_no:
            count = 0
            for j in nums:
                if i == j:
                    count += 1
            data.append((count, i))
        
        data = sorted(data, reverse=True, key=lambda x:[1])

        return [x[1] for x in data[:k]]

