from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        frequency_bucket = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        for num, count in count_dict.items():
            frequency_bucket[count].append(num)

        for i in range(len(frequency_bucket) - 1, 0, -1):
            for num in frequency_bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result
