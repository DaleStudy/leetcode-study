"""
https://leetcode.com/problems/two-sum/

시간 복잡도: O(n²)
- 첫 번째 반복문에서 최대 n번 순회
- 각 숫자마다 뒤의 숫자들을 다시 순회
- 확인하는 숫자 쌍의 개수는 약 n(n - 1) / 2개

공간 복잡도: O(1)
- 입력 크기와 관계없이 i, j 등의 고정된 변수만 사용

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
