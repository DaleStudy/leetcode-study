import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        heap = []
        for k_, v in num_dict.items():
            heapq.heappush(heap, [-v, k_])
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

