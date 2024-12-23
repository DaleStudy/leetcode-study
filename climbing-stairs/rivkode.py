# Time Complexity O(n)
# - traversing for loop takes O(n)
# Space Complexity O(n)
# - appending for loop it takes O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        stage = [1, 2, 3]

        for i in range(3, 45):
            value = stage[i - 1] + stage[i - 2]
            stage.append(value)

        return stage[n - 1]

if __name__ == "__main__":
    solution = Solution()
    result = solution.climbStairs(5)
    print(result)

