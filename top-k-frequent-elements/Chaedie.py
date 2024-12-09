"""
Solution: 
    1. make a dictionary of (index, Frequency)
    2. sort the items of dictionary by Frequency
    3. return list of Top k Frequent Elements

Time Complexity:
    1. iterate nums for counting -> O(n)
    2. sort -> O(n log n)
    3. iterate list for making return value -> O(n)

    So Time complexity of this solution is O(n log n)

Space Complexity: 
    1. dictionary for counting frequency of nums -> O(n)
    2. sorted List -> O(n)

    Space complexity of this solution is O(n)
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        result = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], result[:k]))
