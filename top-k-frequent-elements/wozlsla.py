import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 하나씩 전부 돌면서 빈도수 저장, k개만큼만
        # cnt 함수를 써서 비교후 저장 -> 더 많은 반복?
        # 일단 한번은 다 돌아야함. 가장 적게 돌 수 있는 방법?
        # 전체 순차 비교?

        table = {}

        for i in range(len(nums)):
            table[nums[i]] = table.get(nums[i], 0) + 1

        topk = heapq.nlargest(k, table, key=table.get)
        return topk
