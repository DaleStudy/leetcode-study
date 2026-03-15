from typing import *


class Solution:
    """
    TC: O(n)
    - left 배열 생성: O(n)
    - right 배열 생성: O(n)
    - answer 배열 생성: O(n)
    최종: O(n)

    SC: O(n)
    - left, right, answer 배열 각각 O(n)
    최종: O(n)

    풀이:
    나누기 없이 풀기 위해 각 인덱스 기준 왼쪽 원소들의 곱(left), 오른쪽 원소들의 곱(right) 배열을 별도로 만들고
    answer[i] = left[i-1] * right[i+1] 로 계산.
    i=0이면 왼쪽 곱 없으므로 right[i+1]만, i=마지막이면 left[i-1]만 사용.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        last_index = nums_len - 1

        left = [0] * nums_len
        for i, num in enumerate(nums):
            if i == 0:
                left[i] = num
                continue
            left[i] = left[i - 1] * num

        right = [0] * nums_len
        for i in range(last_index, -1, -1):
            if i == last_index:
                right[i] = nums[i]
                continue
            right[i] = right[i + 1] * nums[i]

        answer = [0] * nums_len
        for i in range(nums_len):
            if i == 0:
                answer[i] = right[i + 1]
                continue
            if i == last_index:
                answer[i] = left[i - 1]
                continue
            answer[i] = left[i - 1] * right[i + 1]

        return answer
