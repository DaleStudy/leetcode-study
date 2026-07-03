from collections import Counter


class Solution:
    # Solution 1
    # Time Complexity: O(nlogn), n: len(nums)
    # Space Complexity: O(n), n:len(nums)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            sorted_nums = sorted(counter, key=lambda num: counter[num])

        return sorted_nums[-k:]

    # Solution 2
    # Time Complexity: O(n), n: len(nums)
    # Space Complexity: O(n), n: len(nums)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, cnt in counter.items():
            buckets[cnt].append(num)

        sorted_nums = [item for bucket in buckets for item in bucket]

        return sorted_nums[-k:]
