"""
[Problem]
https://leetcode.com/problems/house-robber/description/
"""

class Solution(object):
    """
    [Brain Storming]
    같은 날에, 인접한 집을 털면 안된다.
    하루에 털 수 있는 최대 금액을 구하는 문제.

    1 <= nums.length <= 100
    nums.length가 최대 100이기 때문에,
    DFS로 문제를 접근해도 풀 수 있는 문제라고 생각한다.

    각 집을 넣는 경우와 안넣는 경우 인접한 경우를 따져서 최대 금액을 구해보자.

    [Complexity]
    Time: 집을 터는 경우, 안 터는 경우 2^100.. -> Time Limit Exceeded 발생
    Space: O(N) 재귀 호출 스택의 길이도 비례하여 길어짐.
    """
    def rob1(self, nums):
        answer = 0
        visited = [False] * len(nums)

        def dfs(depth, sum):
            # nonlocal nums
            nonlocal answer
            nonlocal visited


            if depth == len(nums):
                answer = max(answer, sum)
                print(sum, visited)
                return

            # 다음 집을 포함한 경우
            if depth == 0 or not visited[depth - 1]:
                visited[depth] = True
                dfs(depth + 1, sum + nums[depth])

            # 다음 집을 포함하지 않은 경우
            visited[depth] = False
            dfs(depth + 1, sum)

        dfs(0, 0)
        return answer

    def rob(self, nums):
        """
        다른 사람의 풀이
        DFS + Memoization 기법을 활용한다.
        ref: https://www.algodale.com/problems/house-robber/

        [Complexity]
        Time: O(N)
        Space: O(N)

        """
        cache = {}
        def dfs(depth):
            if depth in cache:
                return cache[depth]
            if depth >= len(nums):
                cache[depth] = 0
                return cache[depth]

            cache[depth] = max(nums[depth] + dfs(depth + 2), dfs(depth + 1))
            return cache[depth]

        return dfs(0)


sol = Solution()
print(sol.rob([1, 2, 3, 1]))
print(sol.rob([2,7,9,3,1]))

# Edge Case
print(sol.rob([1]) == 1)
print(sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))

