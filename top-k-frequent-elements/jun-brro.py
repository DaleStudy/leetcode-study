class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
