

"""
Time Complexity: O(NLogN)
Space Complexity: O(N) ( Reason: Recursive stack pointer for every element )

Divide and Conquer Approach

1. Divide the array into two halves
2. Find the maximum subarray sum in the left half
3. Find the maximum subarray sum in the right half
4. Find the maximum subarray sum that crosses the midpoint
5. Return the maximum of the three sums
"""
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:

#         def divide(start: int, end: int) -> int:
#             if start >= end:
#                 return nums[start]

#             mid = (start + end) // 2

#             left = divide(start, mid)
#             right = divide(mid + 1, end)

#             left_largest = -float('inf')
#             right_largest = -float('inf')

#             left_acc = 0
#             right_acc = 0

#             left_index = mid
#             right_index = mid + 1

#             while left_index >= start:
#                 left_acc += nums[left_index]
#                 left_largest = max(left_largest, left_acc)
#                 left_index -= 1

#             while right_index <= end:
#                 right_acc += nums[right_index]
#                 right_largest = max(right_largest, right_acc)
#                 right_index += 1

#             return max(left_largest + right_largest, left, right)

#         return divide(0, len(nums) - 1)




"""
Time Complexity: O(N)
Space Complexity: O(1)

prev : maximum sum of the subarray ending with the previous element
ans : maximum sum of the subarray
curr : maximum sum of the subarray ending with the current element
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        prev = nums[0]
        ans = nums[0]

        for i in range(1, N):
            prev = max(nums[i], prev + nums[i])
            ans = max(ans, prev)

        return ans
