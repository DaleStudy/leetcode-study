# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [Complexity]
            - TC: O(n + klogn)
            - SC: O(n)

        [Approach]
            1. nums를 순회하면서 원소별 등장 횟수를 카운트한다.
            2. min heap에 (-등장 횟수, 원소) 형태의 tuple을 저장한다.
            3. k번 pop 하면, k most frequent elements를 얻을 수 있다.
        """
        import heapq
        from collections import Counter

        # 0. early stop
        if len(nums) == k:
            return nums

        # 1. 등장 횟수 카운트
        cnt = Counter(nums)  # -- O(n)

        # 2. min heap에 저장
        q = [(-c, num) for num, c in cnt.items()]  # -- O(n)
        heapq.heapify(q)  # -- O(n)

        # 3. k번 pop
        res = []
        for _ in range(k):  # -- O(k)
            _, num = heapq.heappop(q)  # -- O(logn)
            res.append(num)

        return res
