from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        prefix = 1
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(-1, -n-1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


# 시간 복잡도: O(n)
# - 입력 배열 nums를 두 번 순회합니다.
#
# 공간 복잡도: O(1)
# - 추가 공간으로 사용하는 변수는 prefix와 suffix뿐이며,
#   출력 배열(result)은 추가 공간으로 계산하지 않습니다.
