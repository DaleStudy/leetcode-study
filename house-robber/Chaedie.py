'''
Solution:
    스스로 풀지 못해 학습만 진행했습니다.
    다음 기회에 다시 풀어보도록 하겠습니다.
'''
class Solution:
     def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(num + prev, curr)

        return curr


# class Solution:
    # '''
    # 4. 달레의 코드 풀이 - DP, prev, curr
    # O(n) time
    # O(1) space
    # '''

    # # 달레의 코드 풀이 - DP, prev, cur

    # def rob(self, nums: List[int]) -> int:
    #     prev, curr = 0, 0
    #     for num in nums:
    #         prev, curr = curr, max(num + prev, curr)

    #     return curr

    # '''
    # 3. 달레의 코드 풀이 - DP
    # [1,2,3,1]
    # [1, 2, 3, 1]
    # DP:[0, 1, 2, 4, 4]
    # MAX(1 + DP[2], DP[1]) = MAX(1 + 2, 4) = 4
    # '''
    # # 달레의 코드 풀이 - DP
    # # def rob(self, nums: List[int]) -> int:
    # #     dp = [0] * (len(nums) + 1)
    # #     dp[1] = nums[0]
    # #     for n in range(2,len(nums) + 1):
    # #         dp[n] = max(nums[n - 1] + dp[n - 2], dp[n - 1])
    # #     return dp[-1]
    # '''
    # 2. 달레의 코드 풀이 - 재귀, 메모이제이션
    # time: O(n)
    # space: O(n)
    # '''
    # # 달레의 코드 풀이 - 재귀, 메모이제이션
    # # def rob(self, nums: List[int]) -> int:
    # #     memo = {}
        
    # #     def dfs(start):
    # #         if start in memo:
    # #             return memo[start]
    # #         if not start < len(nums):
    # #             memo[start] = 0
    # #         else:
    # #             memo[start] = max(nums[start] + dfs(start + 2), dfs(start + 1))
    # #         return memo[start]
    # #     return dfs(0)
    # '''
    # 1. 달레의 코드 풀이 - 재귀
    # time: O(2^n)
    # space: O(n)
    
    # F([1,2,3,1]) => MAX(1 + F([3,1], f([2,3,1])))
    #     F([3,1]) => MAX(3 + F([]), F([1]))
    #         F([]) => 0
    #         F([1]) => MAX(1 + F([]), F([])) => MAX(1 + 0, 0) => 1
    #             F([]) => 0
    #             F([]) => 0
    #     F([2,3,1]) => MAX(2 + F([1]), F([3,1]))
    #         F([1]) => MAX(1 + F([]), F([])) => MAX(1 + 0, 0) => 1
    #             F([]) => 0
    #             F([]) => 0
    #         F([3,1]) => MAX(3 + F([]), F([1]))
    #         F([]) => 0
    #         F([1]) => MAX(1 + F([]), F([])) => MAX(1 + 0, 0) => 1
    #             F([]) => 0
    #             F([]) => 0
    # 재귀가 불필요하게 반복되고 있다.
    # 메모이제이션으로 기억해두면 반복은 스킵할 수 있다.
    # '''
    # # 달레의 코드 풀이 - 재귀
    # # def rob(self, nums: List[int]) -> int:
        
    # #     def dfs(start):
    # #         if not start < len(nums):
    # #             return 0
    # #         return max(nums[start] + dfs(start + 2), dfs(start + 1))
    # #     return dfs(0)
        
    # # neetcode 풀이 - DP, 이해안됨...
    # # def rob(self, nums: List[int]) -> int:
    # #     rob1, rob2 = 0, 0
    # #     # [rob1, rob2, n, n+1, ...]
    # #     for n in nums:
    # #         temp = max(n + rob1, rob2)
    # #         rob1 = rob2
    # #         rob2 = temp
    # #     return rob2