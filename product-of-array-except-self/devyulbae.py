"""
Blind75 - 4. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
조건 : 
- 분할 없이 O(n) 시간 복잡도 이하로 풀어라
- nums의 모든 원소의 곱은 32비트 정수 범위 내에 들어온다

0이 몇개인가?
- 2개 이상 : 모두 0인 배열
- 1개 : 0 본인 제외는 0인 배열
- 0개 : 전체 곱 % self 인 배열
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            all_product = 1
            for num in nums:
                all_product *= num if num != 0 else 1

            return [0 if num!= 0 else all_product for num in nums]
        else:
            all_product = 1
            for num in nums:
                all_product *= num
            
            return [all_product // num for num in nums]