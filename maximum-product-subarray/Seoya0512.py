'''
이전 곱을 저장해서 곱셈 연산을 줄이는 방식
해당 연산 방식은 Time Limited Exceeded 오류를 발생했습니다. 

시간 복잡도: O(n^2)
- 외부 for-loop과 내부 for-loop이 각각 n번씩 실행되기 때문
공간 복잡도: O(1)
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]

        for i in range(len(nums)):
            prev = 1
            for j in range(i, len(nums)):
                prev = prev * nums[j]
                max_product = max(max_product, prev)

        return max_product
