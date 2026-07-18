"""
Time Complexity: O(N)
Space Complexity: O(1)

prev_2 : number of ways to decode the string ending with the previous two characters
prev_1 : number of ways to decode the string ending with the previous character
new_prev : number of ways to decode the string ending with the current character
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        if s[0] == "0":
            return 0

        if N == 1:
            return 1

        prev_2 = 1
        prev_1 = int(1 <= int(s[0] + s[1]) <= 26) + int(s[1] != "0")

        for i in range(2, N):
            new_prev = 0
            if 1 <= int(s[i - 1] + s[i]) <= 26 and s[i - 1] != "0":
                new_prev += prev_2
            if s[i] != "0":
                new_prev += prev_1

            prev_2, prev_1 = prev_1, new_prev

        return prev_1
