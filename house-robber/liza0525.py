# 시간 복잡도: O(n)
# - dfs(start_i)는 start_i마다 한 번만 계산됨 (memoization하기 때문)
# - 가능한 start_i 상태는 0 ~ n-1 이므로 총 n개
# 공간 복잡도: O(n)
# - memo dictionary가 최대 n개의 결과를 저장
# - 재귀 DFS 호출 스택 깊이가 최대 n
class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        memo = {}

        def dfs(start_i):
            if start_i in memo:
                # memo에 저장된 정보라면 해당 값을 return
                return memo[start_i]
            
            if start_i >= houses:
                # start_i가 전체 집 개수(len(nums))를 벗어나면 더이상 계산할 이유가 없으므로 0 return
                return 0
            else:
                # start_i에서 시작해서 계산한 최대 비용은
                # start_i + 2에서 시작했을 때의 최대 비용 및 nums[start_i]의 비용의 합과,
                # start_i + 1에서 시작했을 때의 최대 비용을
                # 비교하여 더 큰 값이 된다.

                # 계산한 start_i에서의 최대 비용은 memo에 저장
                memo[start_i] = max(nums[start_i] + dfs(start_i + 2), dfs(start_i + 1))
                return memo[start_i]

        result = dfs(0)
        return result
