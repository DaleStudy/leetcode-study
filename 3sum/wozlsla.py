"""
# Intuition
-

# Approach
index가 모두 다를것,
합 = 0 -> -a = b+c
중복 X -> set : dic와 다르게 가변객체 삽입 X
Two Pointer -> 정렬된 배열을 활용

# Complexity
- Time complexity
  - Brute-force : O(N^3)
  - Set : O(N^2) - Time Limit Exceeded (memory??)
  - Two Pointer : O(N^2)

- Space complexity
  - Brute-force : O(N)
  - Set : O(N)
  - Two Pointer : O(1)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = set()
        nums.sort()  # O(NlogN), return None

        for i in range(len(nums) - 2):  # O(N)
            low, high = i + 1, len(nums) - 1

            while low < high:  # O(N)
                three_sum = nums[i] + nums[low] + nums[high]

                if three_sum < 0:
                    low += 1
                elif three_sum > 0:
                    high -= 1
                else:
                    triplets.add((nums[i], nums[low], nums[high]))
                    low, high = low + 1, high - 1

        return list(triplets)


""" Set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = set()

        for i in range(len(nums) - 2):
            seen = set()

            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])

                if complement in seen:
                    triplets.add(tuple(sorted([nums[i], nums[j], complement])))

                seen.add(nums[j])

        return list(triplets)
"""

""" Brute-force
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result = []

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if i != j and i != k and j != k:
                    
                        if nums[i] + nums[j] + nums[k] == 0:
                            li = sorted([nums[i], nums[j], nums[k]])

                            if li not in result: # O(L)
                                result.append(li)

        return result
"""

nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()

print(sol.threeSum(nums))
# [[-1,-1,2],[-1,0,1]]

# print(len({1, 1, 2})) # 2
