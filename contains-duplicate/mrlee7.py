from typing import List


class Solution:
    """
    Ideation:
        각 원소가 발견되면 hash map 에 해당하는 item 기반으로 flag를 세운다.
        해당 인덱스에서 flag가 이미 켜져있다면, 앞에서 탐색된 원소이므로 True를 반환한다.
        마지막까지 다 돌았는데 중복된 케이스가 없다면 False를 반환한다.
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        return False
