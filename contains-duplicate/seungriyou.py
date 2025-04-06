# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        """
        [Complexity]
            - TC: O(n) (set(nums) 시 원소를 복사하는 데에 O(n), len()은 O(1))
            - SC: O(n)

        [Approach]
            set(hash map)을 이용하여 중복을 제거한 결과의 길이를 원본 리스트의 길이와 비교하면 된다.
        """

        return len(nums) != len(set(nums))


    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        [Complexity]
            - TC: O(n) (iteration)
            - SC: O(n)

        [Approach]
            nums를 순회하면서 set(hash map)에 등장했던 원소를 add 하고, 동일한 원소가 발견되면 True를 반환한다.
            nums 전체를 순회하면서 동일한 원소가 없었다면 False를 반환한다.
        """

        seen = set()

        for num in nums:    # -- O(n)
            if num in seen: # -- O(1)
                return True
            seen.add(num)

        return False
