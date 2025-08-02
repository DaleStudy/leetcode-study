"""
# Intuition
하나씩 순회하면서 나머지 값들을 곱함

# Approach
접근 1) 원형 큐를 사용하면?
현재 제외하려는 요소를 popleft()로 제거하고, 나머지 요소들의 곱을 계산한 뒤, 다시 그 요소를 append()하여 다음 반복을 위해 덱의 순서를 회전

접근 2)
1 b c d --> 1 x bcd
a 1 c d --> a x  cd
a b 1 d --> ab x  d
a b c 1 --> abc x 1


# Complexity
- Time complexity : O(N)
- Space complexity : O(N) / O(1)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [1] * n

        prefix_product = 1
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix_product
            suffix_product *= nums[i]


"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 중복 계산을 피하는 방법?
        res_1 = [1] * len(nums) 
        res_2 = [1] * len(nums)

        for n in range(1, len(nums)):  # [1, 1(a), 2(ab), 6(abc)]
            res_1[n] = res_1[n - 1] * nums[n - 1]

        # reverse X -> range를 반대로
        for n in range(len(nums) - 1, -1, -1):  # [1, 4(d), 12(cd), 24(bcd)]
            res_2[n] = res_2[n + 1] * nums[n + 1]

        res_2.reverse()
        return [res_1[i] * res_2[i] for i in range(len(nums))]


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
"""


"""
# deque : O(N^2)
from collections import deque
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        nums = deque(nums)
        result = []

        for _ in range(len(nums)): # O(N)
            tmp = nums.popleft()
            result.append(math.prod(nums)) # O(N)
            nums.append(tmp)
        
        return result
"""
