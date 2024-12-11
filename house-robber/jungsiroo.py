class Solution:
    def bfs(self, nums):
        from collections import deque
        queue = deque()

        # price, idx, robbed prev
        queue.append([0, 0, False])
        queue.append([0, 0, True])
        ret = 0

        while queue:
            price, idx, prev = queue.popleft()
            ret = max(ret, price)
            if idx == len(nums):
                continue
            
            if prev: 
                queue.append([price, idx+1, False])
            else:
                queue.append([price, idx+1, False])
                queue.append([price+nums[idx], idx+1, True])

        return ret 
    
    def rob(self, nums: List[int]) -> int:
        # BFS - Slow and out of memory
        """return self.bfs(nums)"""

        # DP
        n = len(nums)
        record = [[0]*n for _ in range(2)]
        record[1][0] = nums[0]

        for i in range(1, n):
            record[1][i] = max(record[0][i-1]+nums[i], record[1][i])
            record[0][i] = max(record[1][i-1], record[0][i-1])

        return max(record[1][-1], record[0][-1])

