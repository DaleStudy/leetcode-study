# TC : O(n)
# SC : O(n)
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize a list of empty lists to store numbers based on their frequencies
        freq = [[] for i in range(len(nums) + 1)]

        # Dictionary to count the frequency of each number
        counter = defaultdict(int)

        # Count the frequency of each number in nums
        for num in nums:
            counter[num] += 1

        # Group numbers by their frequency
        for n, c in counter.items():
            freq[c].append(n)

        # Result list to store the top k frequent elements
        res = []

        # Iterate over the frequency list in reverse order to get the most frequent elements first
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # Once we have k elements in the result, return it
                if len(res) == k:
                    return res
