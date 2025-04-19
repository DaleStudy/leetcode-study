# O(log n) time, O(1) space
# % 나머지, // 몫 

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        while n > 0:
            if (n % 2) == 1:
                cnt += 1
            n //= 2

        return cnt
    

# O(log n) time, O(log n) space
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
    

# TS 풀이
# O(log n) time, O(log n) space
# function hammingWeight(n: number): number {
#     return n.toString(2).split('').filter(bit => bit === '1').length;
# };
