class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        results = list(map(lambda x: x[0], sorted(num_dict.items(), key=lambda x: -x[1])))
        return results[:k]
