"""
# Intuition
N is can be up to 100000, so time complexity should be O(N log N) at least.
Calculate the frequency of its elements using dictionary, sort it, and list top K ones.

# Approach
1. for n in nums:
    1-1. if n in map: map[n] += 1
2. sort it by its value
3. slice and return top K

# Complexity
Let:
- N = len(nums)
- M = number of unique elements in nums

Time complexity:
- O(N) + O(M log M) + O(K)
- O(N log N) when all elements are unique.

Space complexity:
- O(M) + O(M) + O(K)
- Overall: O(N) in the worst case.
"""

from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        value_sorted = sorted(dic.items(), key=lambda x: -x[1])
        return [i[0] for i in value_sorted[:k]]
