class Solution:
    # dictionary use 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}  # key: 원소, value: 등장 횟수
        for n in nums:
            if n in result:
                result[n] = result[n] + 1
            else:
                result[n] = 1

        # 가장 자주 등장한 원소 k개 반환
        return sorted(result.keys(), key=lambda x: result[x], reverse=True)[:k]
