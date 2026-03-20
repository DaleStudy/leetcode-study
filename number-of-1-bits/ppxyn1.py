# idea: - 

# Ans 1
# Time Complexity: O(N) ?
from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n).split('0b')[-1]
        return Counter(bits)['1']



# Ans 2
# Time Complexity: O(N) 
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n & 1 # check current bit
            n >>= 1 # move to next bit
        return cnt

