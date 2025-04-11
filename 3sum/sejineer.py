"""
시간 복잡도: O(N^2)
공간 복잡도: O(N)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = set()

        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            while start < end:
                temp = nums[i] + nums[start] + nums[end]
                if temp == 0:
                    result.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif temp < 0:
                    start += 1
                else:
                    end -= 1

        return list(result)
