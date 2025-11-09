class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        items = counts.items()

        sort_by_value = sorted(
            items,
            key=lambda item: item[1],
            reverse = True
        )
        result = []
        for i in range(k):
            result.append(sort_by_value[i][0])
        return result
        