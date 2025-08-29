from bisect import bisect_left

class Solution:
    """
    뭔가 bfs 풀이 방식
    메모리 초과
    """
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     q = deque()
    #     q.append((-1, float('-inf'), 0))  # (idx, lastValue, length)
    #     answer = 0
        
    #     while q:
    #         idx, last, length = q.popleft()
    #         answer = max(answer, length)
            
    #         for nxt in range(idx + 1, n):
    #             if nums[nxt] > last:
    #                 q.append((nxt, nums[nxt], length + 1))
        
    #     return answer

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     dp = [1] * len(nums)
    #     for cur in range(1, len(nums)):
    #         for pre in range(cur):
    #             if nums[pre] < nums[cur]:
    #                 dp[cur] = max(1 + dp[pre], dp[cur])
    #     return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            index = bisect_left(sub, num)
            if index == len(sub):
                sub.append(num)
            else:
                sub[index] = num
        return len(sub)
