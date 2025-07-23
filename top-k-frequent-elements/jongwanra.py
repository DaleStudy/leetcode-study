"""
[Problem]
https://leetcode.com/problems/top-k-frequent-elements/

[Brain Storming]
가장 자주 사용되는 요소 k개를 반환한다.

1<= nums.length <= 10^5
O(n^2) time complexity일 경우 시간 초과 발생

[Plan]
1. nums를 순회하면서 Hash Table에 key:element value:count 저장한다.
2. nums를 순회하면서 Heap에 (count, element)를 count를 기준으로 Max Heap 형태로 저장한다.
3. Max Heap에서 k개 만큼 pop한다.

[Complexity]
N: nums.length, K: k
heapq.heapify(heap): O(N)
heapq.heappop(heap): log(N)

Time: O(N +  (K * log(N)))
Space: O(N + K)
    * num_to_count_map: O(N)
    * heap: O(N)
    * answer: O(K)


"""

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        num_to_count_map = {}
        for num in nums:
            num_to_count_map[num] = num_to_count_map.get(num, 0) + 1

        heap = []
        for num, count in num_to_count_map.items():
            heap.append((-count, num))
        heapq.heapify(heap)

        answer = []
        for _ in range(k):
            negative_count, frequent_num = heapq.heappop(heap) # log(N)
            answer.append(frequent_num)
        return answer

solution = Solution()

# Normal Case
print(solution.topKFrequent([1,1,1,2,2,3], 2) == [1, 2])
print(solution.topKFrequent([1], 1) == [1])


