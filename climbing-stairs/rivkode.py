# Time Complexity O(n)
# - traversing for loop takes O(n)
# - same with 피보나치
# Space Complexity O(n)
# - appending for loop it takes O(n)

class Solution:

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        map = {1:1, 2:2}


        for i in range(3, n + 1):
            map[i] = map[i-1] + map[i-2]
        
        return map[n]


    # def climbStairs(self, n: int) -> int:
    #     stage = [1, 2, 3]

    #     for i in range(3, 45):
    #         value = stage[i - 1] + stage[i - 2]
    #         stage.append(value)

    #     return stage[n - 1]

if __name__ == "__main__":
    solution = Solution()
    result = solution.climbStairs(5)
    print(result)





