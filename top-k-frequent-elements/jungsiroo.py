class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive Solution
        # TC : O(nlogn)
        # SC : O(n)
        
        cnt = dict()
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
            
        """
        ret = dict(sorted(cnt.items(), key=lambda x:(-x[1], x[0])))
        return list(ret.keys())[:k]
        """

        # Follow up Solution
        # TC : O(nlog(k))
        # SC : O(n)

        import heapq

        ret = [(-c, num) for num, c in cnt.items()]
        heapq.heapify(ret)

        return [heapq.heappop(ret)[1] for _ in range(k)]
        
