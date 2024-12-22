"""
solution 1:
    왼쪽부터 곱해가는 prefix,
    오른쪽부터 곱해가는 postfix,
    2가지의 배열을 만든다.

    nums = [1,2,3,4]
    prefix = [1,2,6,24]
    postfix = [24,12,4,1]

    이후 정답 배열 result[i] = prefix[i - 1] * postfix[i + 1] 이 되도록 만든다.
    0, n-1 번째 인덱스에선 예외처리를 해준다.

Time: O(n) = prefix 계산 O(n) + postfix 계산 O(n) + result 계산 O(n)
Space: O(n) = prefix 배열 O(n) + postfix 배열 O(n)
"""

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)

#         prefix = [1 for i in range(n)]
#         postfix = [1 for i in range(n)]

#         prefix[0] = nums[0]
#         for i in range(1, n):
#             prefix[i] = prefix[i-1] * nums[i]

#         postfix[n - 1] = nums[n - 1]
#         for i in range(n-2, -1, -1):
#             postfix[i] = postfix[i + 1] * nums[i]

#         result = []
#         for i in range(n):
#             pre = prefix[i - 1] if i - 1 >= 0 else 1
#             post = postfix[i + 1] if i + 1 < n else 1
#             result.append(pre * post)
#         return result

"""
최적화 풀이 
Solution:
    prefix, postfix 배열 저장 없이 순회하며 바로 prefix, postfix 를 곱해서 result 배열에 담는다.

Time: O(n) = O(2n)
Space: O(1)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
