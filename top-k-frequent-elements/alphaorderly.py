class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)

        cntr_list = [(-b, a) for a, b in list(cntr.items())]

        heapify(cntr_list)

        ans = []

        for _ in range(k):
            ans.append(heappop(cntr_list)[1])

        return ans
