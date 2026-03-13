
# 6기 
# class Solution:
#     # dictionary use 
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         result = {}  # key: 원소, value: 등장 횟수
#         for n in nums:
#             if n in result:
#                 result[n] = result[n] + 1
#             else:
#                 result[n] = 1

#         # 가장 자주 등장한 원소 k개 반환
#         return sorted(result.keys(), key=lambda x: result[x], reverse=True)[:k]

# 7기 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequency of each number
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        # 2. Sort by frequency in descending order
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        # 3. Take the first k elements
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result
