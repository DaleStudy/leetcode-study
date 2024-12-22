# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count how many times each number appears
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # sort numbers by their count (most frequent first) and grab top k
        # counts.get gets the count of num
        # reverse=True sorts in descending order
        # [:k] gets the first k elements
        top_nums = sorted(counts, key=counts.get, reverse=True)
        return top_nums[:k]
