# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n) (unique_nums)

        [Approach]
            O(n) time에 돌아가야 하므로 O(nlogn)인 sorting은 사용할 수 없다.
            그리고 integer에서 consecutive 라는 것은 1 차이라는 것이다.
            따라서 hash map에서 현재 보고 있는 num 값에 대해 left(= num - 1)와 right(= num + 1)를 O(1) time에 찾아보는 방식으로 접근해야 한다.
            이때, left와 right를 양옆으로 확장시켜가면서 max_length = max(max_length, right - left - 1)로 업데이트 한다.
        """

        max_length = 0
        unique_nums = set(nums)

        for num in nums:
            # num의 consecutive integer인 left, right 구하기
            left, right = num - 1, num + 1

            # left, right 양옆으로 확장하며 unique_nums에서 지워나가기
            while left in unique_nums:
                unique_nums.remove(left)
                left -= 1
            while right in unique_nums:
                unique_nums.remove(right)
                right += 1

            # 현재 보고 있는 num이 속하는 consecutive sequence의 length는 (right - left - 1)
            max_length = max(max_length, right - left - 1)

            # unique_nums가 비었으면, 더이상 확인할 필요가 없음
            if not unique_nums:
                break

        return max_length

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n) (unique_nums)

        [Approach]
            첫 번째 풀이와 비슷하나, unique_nums를 순회하다가 현재 보고 있는 num이 자신이 속한 consecutive sequence의 가장 left 값일 때만
            오른쪽으로 확장한다는 점에서 약간 다른 풀이이다.
            이때, 오른쪽으로 확장 후 max_length = max(max_length, right - num)로 업데이트 한다.
        """

        max_length = 0
        unique_nums = set(nums)

        for num in unique_nums:
            # 현재 보고 있는 num이, 자신이 속한 consecutive sequence의 가장 left 값이라면,
            if num - 1 not in unique_nums:
                # 오른쪽으로 확장하기
                right = num + 1
                while right in unique_nums:
                    right += 1

                # 현재 보고 있는 num이 첫 번째 값인 consecutive sequence의 length는 (right - num)
                max_length = max(max_length, right - num)

        return max_length
