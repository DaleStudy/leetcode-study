"""
# Approach
모든 원소끼리 곱한 다음에 nums 배열을 순회하며 그 값을 해당 원소로 나눈다.
이때 0의 개수와 0을 제외한 곱의 값도 같이 구한다.
0이 2개 이상이면 정답은 모두 0이며,
0이 1개면 0을 제외한 곱의 값을 사용한다.

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)
"""


# Code
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        non_zero_product = 1
        zero_count = 0
        for num in nums:  # O(n) Time complexity
            if num == 0:
                zero_count += 1
                non_zero_product *= 1
            else:
                non_zero_product *= num
            product *= num

        if zero_count > 1:
            return [0] * len(nums)  # O(n) space complexity

        answer = []  # O(n) space complexity
        for i in range(len(nums)):  # O(n) Time complexity
            if nums[i] == 0:
                answer.append(non_zero_product)
            else:
                answer.append(int(product / nums[i]))
        return answer
