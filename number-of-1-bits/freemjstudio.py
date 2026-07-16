class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        return binary.count("1")

# bin() 을 못쓰는 경우의 풀이
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            count += n % 2
            n //=2

        return count
