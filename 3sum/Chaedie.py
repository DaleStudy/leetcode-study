"""
첫번째 풀이 -> 달레의 코드 풀이
1) sort와 two pointer를 활용한 풀이
2) has_set 을 활용한 중복 제거

두번째 풀이 -> Neetcode 풀이
1) sort와 two pointer를 활용한 풀이
2) while loop 를 활용한 중복 제거

Time: O(n) = O(n) + O(n)
Space: O(n)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
        return list(res)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            l, r = i + 1, n - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
