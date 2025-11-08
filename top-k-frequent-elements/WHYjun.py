class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time complexity: O(nlog(n))
        # Space Complexity: O(n)

        if len(nums) <= k:
            return list(set(nums))

        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        
        # The key of dictionary is unique.
        sortedKeys = sorted(list(counts.keys()), key=lambda key: counts[key], reverse = True)
        return sortedKeys[:k]
