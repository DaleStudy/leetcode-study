"""
Title: 237. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/

Question:
    - Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
    - You may return the answer in any order.

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - k is in the range [1, the number of unique elements in the array].
    - The answer is guaranteed to be unique.

Time Complexity:
    - O(n log n)
Space Complexity:
    - O(n)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(sorted_frequency[i][0])
        return result
    