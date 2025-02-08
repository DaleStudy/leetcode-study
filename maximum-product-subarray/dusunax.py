'''
# 152. Maximum Product Subarray

solution reference: https://www.algodale.com/problems/maximum-product-subarray/

## 최대 곱 배열 구하기
- 연속 배열(subarray)에 양수, 음수, 0이 포함될 수 있다.
- 음수가 결과에 영향을 미칠 수 있기 때문에 최소값/최대값 추적이 필요하다.

## 값
- result: 최종적으로 반환할 값
- min_prod: 현재까지의 최소 곱 값 (음수를 고려한 추적)
- max_prod: 현재까지의 최대 곱 값

## 새로운 값 num이 주어졌을 때
- 새로운 배열을 시작할 지, 기존 배열에 추가할 지 결정
- 후보들로 최대값의 가능성을 확인하고 result를 업데이트한다.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        min_prod = 1
        max_prod = 1

        for num in nums:
            candidates = (min_prod * num, max_prod * num, num)
            min_prod = min(candidates)
            max_prod = max(candidates)
            result = max(max_prod, result)

        return result