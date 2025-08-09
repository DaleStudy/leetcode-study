"""
[Problem]
https://leetcode.com/problems/climbing-stairs/

[Brainstorming]
한 번에 갈 수 있는 계단: 1 or 2
갈 수 있는 경우의 수를 구해야 하는 문제
constraints: 1 <= n <= 45

n = 1, 1
n = 2, 2
n = 3, 3
n = 4, 5
...
f(n) = f(n - 1) + f(n - 2)

[Plan]
1. n + 1 크기의 list를 만든다.
2. list[1] = 1, list[2] = 2를 대입한다.
3. for-loop를 3부터 n까지 순회한다.
    3-1. Bottom-Top 방식으로 n까지 값을 채워간다.
4. n값을 반환한다.

[Complexity]
Time: O(n)
Space: O(n)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        answer = [0, 1, 2]
        for index in range(3, n + 1):
            answer.append(answer[index - 1] + answer[index - 2])

        return answer[n]

    """
    another solution
    ref: https://www.algodale.com/problems/climbing-stairs/
    [Summary]
    Bottom Top 방식인데 공간을 최적화하여 접근
    [Complexity]
    Time: O(n)
    Space: O(1) - Space Optimization

    [Plan]
    1. prev = 1, cur = 2를 저장한다.
    2. for-loop를 순회한다. 3 to n + 1

    """

    def climbStairs2(self, n: int) -> int:
        if n <= 3:
            return n

        prev, cur = [2, 3]
        for index in range(4, n + 1):
            tmp = cur
            cur = cur + prev
            prev = tmp
        return cur

    """
    another solution
    ref: https://www.algodale.com/problems/climbing-stairs/
    [Summary]
    Top-Bottom으로 재귀적으로 접근
    [Complexity]
    Time: O(n)
    Space: O(n)
    """

    def climbStairs3(self, n: int) -> int:
        cache = {}

        def dfs(num: int) -> int:
            nonlocal cache
            if num <= 3:
                return num
            if num in cache:
                return cache[num]
            cache[num] = dfs(num - 1) + dfs(num - 2)
            return cache[num]

        return dfs(n)


sol = Solution()

# Normal Case
print(sol.climbStairs3(2) == 2)
print(sol.climbStairs3(3) == 3)
print(sol.climbStairs3(4) == 5)
print(sol.climbStairs3(5) == 8)
print(sol.climbStairs3(38))
# Edge Case
print(sol.climbStairs3(1) == 1)
