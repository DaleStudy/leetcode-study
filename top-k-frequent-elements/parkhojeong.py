class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,1,1,2,2,3] -> {1:3, 2:2, 3:1}
        freqency_dict = {}
        for num in nums:
            freqency_dict[num] = freqency_dict.get(num, 0) + 1

        # {1:3, 2:2, 3:1} -> [[1,3], [2,2], [3,1]]
        frequency_list: List[(int, int)] = []
        for num in freqency_dict:
            frequency_list.append((num, freqency_dict[num]))

        # [[1,3], [2,2], [3,1]] -> [[1,3], [2,2], [3,1]]
        sorted_list = sorted(frequency_list, key=lambda x: x[1], reverse=True)

        return [num[0] for num in sorted_list[:k]]
