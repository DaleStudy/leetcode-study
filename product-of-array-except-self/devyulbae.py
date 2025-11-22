"""
Blind75 - 4. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
조건 : 
- 분할 없이 O(n) 시간 복잡도 이하로 풀어라
- nums의 모든 원소의 곱은 32비트 정수 범위 내에 들어온다
- 나눗셈 금지

0이 몇개인가?
- 2개 이상 : 모두 0인 배열
- 1개 : 0 본인 제외는 0인 배열
- 0개 : 좌 우 각각의 메모이제이션을 해주면 O(2n)으로 배열 생성, O(n)으로 정답 배열 생성하므로 O(n)
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
            left_product = [nums[0]]
            right_product = [nums[-1]]
            for i in range(1,len(nums)): 
                left_product.append(left_product[i-1]*nums[i])
                right_product.append(right_product[i-1]*nums[-1-i])
            
            answer = []
            for i in range(len(nums)):
                answer.append((left_product[i-1] if i>0 else 1)* (right_product[-1-i] if i < len(nums)-1 else 1))
            return answer