from typing import List


class Solution:
    """
    Ideation:
        target = x + y -> target - x = y
        x 원소를 가장 바깥의 이터레이션에서 돌면서 하나씩 대입합니다.
        찾고자 하는 값이 (x,y) 쌍이므로, 두개의 인덱스를 찾기 위해 인덱스 기준으로 이터레이션을 수행합니다( enumerate 사용 가능).
        y값이 찾아지면 당시의 x값의 인덱스와 함께 (index_of_x, index_of_y) 를 리스트로 반환합니다.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (target - nums[i]) == nums[j]:
                    return [i, j]
