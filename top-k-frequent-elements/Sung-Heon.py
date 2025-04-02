class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for i in nums:
            if temp.get(i):
                temp[i] += 1
            else:
                temp[i] = 1
        return [key for key, value in sorted(temp.items(), key=lambda x: x[1],reverse=True)][:k]