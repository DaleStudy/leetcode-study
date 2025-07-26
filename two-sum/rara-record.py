from typing import List

"""
문제 설명:
nums에서 두 수를 더해 target이 되는 두 인덱스를 찾아 반환하는 문제
같은 원소를 두 번 쓸 수 없음
찾야야하는 값: taget - 현재 숫자 = 더해서 target이 되는 값

nums = [2,7,11,15], target = 9
{
  2: 0, (value: index)
  7: 1,
  11: 2,
  15: 3,
}

1. nums를 한 번 순회하며 각 숫자와 인덱스를 딕셔너리에 저장
2. 다시 nums를 순회하며, target - 현재 숫자가 딕셔너리에 있고 인덱스가 다르면 정답 쌍을 반환
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for key, value in enumerate(nums):
            dic[value] = key

        # 다시 nums를 순회
        for key, value in enumerate(nums):
            match = target - value

            # 같은 원소를 두번 쓸 수 없다.
            if (match in dic) and key != dic[match]:
                return [key, dic[match]]

"""
시간 복잡도: O(n)
- 리스트를 두 번 순회하지만 각각 O(n)이 소요되므로, 총 시간 복잡도는 O(n)
공간 복잡도: O(n)
- 입력 크기가 n이라면 딕셔너리의 크기도 최대 n
"""

