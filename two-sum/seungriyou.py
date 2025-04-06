# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            항상 하나의 정답이 존재하기 때문에, 복잡도를 O(n^2)보다 줄이기 위해서는 hash map에 (target - num) 값을 저장함으로써
            현재 보고있는 값과 더했을 때 target이 되는 값을 찾는 과정에 드는 복잡도를 O(1)으로 줄일 수 있다.
                1. nums를 순회하며, hash map의 key에 현재 값이 존재하는지(= 현재 값과 더했을 때 target이 되는 값이 있는지) 확인한다.
                2. 존재한다면, 현재 값의 index와 hash map의 value에 기록되어 있는 index를 반환한다.
                3. 존재하지 않는다면, hash map에 {(target - num): index}를 추가한다.
        """

        remains = dict()

        for i, num in enumerate(nums):
            if num in remains:
                return [remains[num], i]

            remains[target - num] = i
