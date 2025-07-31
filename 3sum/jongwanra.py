"""
[Problem]
https://leetcode.com/problems/3sum/description/

[Brainstorm]
3 <= nums.length <= 3,000
Brute Force: O(N^3) => 27,000,000,000 => time limited
O(N^2)의 풀이는 시간 제한에 걸리지 않을 것으로 보인다. 3,000 * 3,000 => 9,000,000

[Plan]
1. map을 설정한다. key = elements value: index list
2. nested-loop을 순회한다.
    2-1. i == j인 경우 제외
    2-2. map에서 동일한 인덱스인 경우 제외하고 구한다.

"""

from typing import List


class Solution:
    """
    Attempt-1 My solution (incorrect)
    time limited
    """

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        map = {}
        for index in range(len(nums)):
            values = map.get(nums[index], [])
            values.append(index)
            map[nums[index]] = values

        triplets = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                complement = -(nums[i] + nums[j])
                # print(f"nums[{i}]={nums[i]}, nums[{j}]={nums[j]} , complement={complement}")
                if complement in map:
                    values = map[complement]
                    for k in values:
                        if k == i or k == j:
                            continue
                        triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return list(triplets)

    """
    Attempt-2 Another solution
    ref: https://www.algodale.com/problems/3sum/

    """

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for index in range(len(nums) - 2):
            seen = set()
            for j in range(index + 1, len(nums)):
                complement = -(nums[index] + nums[j])
                if complement in seen:
                    triplet = [nums[index], nums[j], complement]
                    triplets.add(tuple(sorted(triplet)))
                seen.add(nums[j])

        return list(triplets)

    """
    Attempt-3 Another solution
    ref: https://www.algodale.com/problems/3sum/

    [Plan]
    two-pointer로 접근한다.

    [Complexity]
    N: nums.length
    Time: O(N^2)
    Space: O(1)
    """

    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()

        for index in range(len(nums) - 2):
            left = index + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[index] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                    continue
                if three_sum > 0:
                    right -= 1
                    continue
                triplets.add((nums[index], nums[left], nums[right]))
                left += 1
                right -= 1
        return list(triplets)


sol = Solution()
print(sol.threeSum3([-1, 0, 1, 2, -1, 4]))

