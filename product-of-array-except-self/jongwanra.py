"""
[Problem]
https://leetcode.com/problems/product-of-array-except-self/

배열 nums가 주어졌을 때, 배열 answer를 반환해라.
answer[i]는 nums[i]를 제외한 모든 요소들의 곱이어야 한다.

[Brainstorming]
전체 요소들의 곱을 구한다. 해당 요소만 나눗셈으로 제외한다.
-> 이 방식은 다루기 어렵다. 0이 들어갈 수 있음.

Brute Force 방식으로 밖에 떠오르지 않음..
O(n)으로 어떻게 풀 수 있지?

"""
from typing import List
class Solution:
    """
    another solution
    ref: https://www.algodale.com/problems/product-of-array-except-self/

    [Brainstorming]
    각 인덱스 요소를 제외한 요소들의 곱은 아래와 같다.
    nums[0] * nums[1] * ... * nums[index - 1] * nums[index + 1] * ... nums[len(nums) - 1]
    즉, nums[index] 전의 곱을 누적한 배열과, nums[index] 이후의 곱을 누적한 배열을 구하면 답을 구할 수 있다.

    [Complexity]
    N: nums.length
    Time: O(N)
    Space: O(N)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before_products = [1] * len(nums)
        for index in range(1, len(nums)):
            before_products[index] = before_products[index - 1] * nums[index- 1]

        after_products = [1] * len(nums)
        for index in range(len(nums) - 2, -1, -1):
            after_products[index] = after_products[index + 1] * nums[index + 1]

        answer = []
        for index in range(len(nums)):
            answer.append(before_products[index] * after_products[index])

        return answer

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
print(sol.productExceptSelf([-1,1,0,-3,3]))
print(sol.productExceptSelf([2,3,4,5]))


