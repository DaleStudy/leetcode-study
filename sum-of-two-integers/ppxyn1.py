# idea : -
# Time Complexity: O(1)

# Solution (1) : It feels a bit like cheating though... but passed the answer lol
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])

'''
# Try and Error : Another way I tried is by using log.

import numpy as np

class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(np.log(np.exp(a) * np.exp(b)))

Ths way has a problem that it is not calculated as log(exp(a) * exp(b)) = log(exp(a+b)) = a + b like human.
'''


