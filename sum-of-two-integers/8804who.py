import math
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log(2**a * 2**b, 2))
    
