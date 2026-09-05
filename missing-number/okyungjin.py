'''
https://leetcode.com/problems/missing-number/description/
'''

'''
solution1: 정렬 후 이진탐색

n: len(nums)
Time: O(n log n), sort
Space: O(1)
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort() # Time: O(n log n)

        left = 0
        right = len(nums)

        while left < right: # Time: O(log n)
            mid = (left + right) // 2

            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1

        return left

'''
solution2: 0부터 n까지 더한 값에서 배열의 전체 합을 빼기

n: len(nums)
Time: O(n)
Space: O(1)
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        complete_sum = n * (n + 1) // 2
        actual_sum = sum(nums) # Time: O(n)

        return complete_sum - actual_sum
