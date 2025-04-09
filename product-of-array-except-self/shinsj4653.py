"""
Inputs: 정수형 배열 nums

Outputs: 정수형 배열 answer

Constraints: 2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Time Complexity: 반드시 o(n)

answer의 각 원소는 본인을 제외한 나머지 원소들 곱한 결과

나눗셈 연산도 불가능
사전?
1 2 3 4
2 4 6 8
6 12 18 24
24 48 72 96

dict[0] :
dict[1] :
dict[2] :
dict[3] :

스택?? push, pop 하는데 o(1) 걸림

(1,0) (2,1) (3,2) (4,3)

스택에서 뺀 다음, 다시 넣으면 while st에 갇히지 않나?

# 풀이 본 이후

nums 1 2 3 4

1 1 1 1

1 1 2 6 : 기준 idx 전까지의 곱

24 12 4 1 : 기준 idx 후까지의 곱

=> 더 개선된 풀이: 누적곱을 덮어씌우는 방법

6
24 12 8 6

24


Space Complexity: O(1)
product 배열에 곱 결과를 덮어씌워도 무방

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = [1 for _ in range(len(nums))]

        before = 1
        for i in range(len(nums) - 1):
            before *= nums[i]
            products[i + 1] *= before

        after = 1
        for i in range(len(nums) - 1, 0, -1):
            after *= nums[i]
            products[i - 1] *= after

        return products
