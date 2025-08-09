"""
[Problem]
https://leetcode.com/problems/number-of-1-bits/description/

양수 n이 주어졌을 때, 이진법에서 1로 설정된 비트의 개수를 반환하는 함수를 작성해라.


[Plan]
1. 주어진 양수를 이진수로 변환한다.
2. for-loop을 순회하며 1의 개수를 counting한다.

[Complexity]
N: bin(n).length - 2
Time: O(N)
Space = O(N)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        output = 0
        for index in range(2, len(binary)):
            if binary[index] == '1':
                output += 1
        return output
"""
ref: https://www.algodale.com/problems/number-of-1-bits/
[Complexity]
Time: O(log n)
Space: O(1)
"""
class AnotherSolution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            quotient, remainder = divmod(n, 2)
            print(f"n = {n} quotient={quotient}, remainder={remainder}")
            count += remainder
            n = quotient
        return count

sol = AnotherSolution()
print(sol.hammingWeight(11) == 3)
print(sol.hammingWeight(128) == 1)
print(sol.hammingWeight(2147483645) == 30)

