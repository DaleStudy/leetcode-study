from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return [num for num, _ in count.most_common(k)]
