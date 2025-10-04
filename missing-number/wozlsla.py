from typing import List


"""
distinct
두 배열의 차이 -> 순회를 어떻게? -> 리스트 > 해시테이블 (t)

# Sol 1

시간 복잡도: O(n)
- 1. Set 생성: O(n)
- 2. 반복문 + 해시셋 검사: O(n) + O(1)

공간 복잡도: O(n)

# Sol 2

시간 복잡도: O(n)
- 1. 0부터 n까지의 전체 합 계산: O(1)
- 2. nums 배열 요소들의 합 계산: O(n)
- 3. 차이가 사라진 숫자: O(1)

공간 복잡도: O(1)

"""


# Sol 1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        table = set(nums)

        for i in range(0, len(nums) + 1):
            if i not in table:
                return i
            else:
                continue


# Sol 2)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # 0부터 n까지의 전체 합 (가우스 공식)
        sum_total = n * (n + 1) // 2

        # nums 배열 요소들의 합
        sum_nums = sum(nums)

        return sum_total - sum_nums
