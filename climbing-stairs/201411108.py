# TC: O(n), 최대 n번 반복 실행
# SC: O(n), 최대 n 길이의 리스트
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        climb_ways = [0 for _ in range(n + 1)]

        climb_ways[0] = 0
        climb_ways[1] = 1
        climb_ways[2] = 2
 
        for i in range(3, n + 1):
            climb_ways[i] = climb_ways[i - 1] + climb_ways[i - 2]

        return climb_ways[n]

