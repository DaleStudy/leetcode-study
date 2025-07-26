class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        frequent_dict = defaultdict(int)
        for num in nums:
            frequent_dict[num] += 1
        sorted_dict = dict(sorted(frequent_dict.items(), key=operator.itemgetter(1), reverse=True))
        return list(sorted_dict)[:k]
