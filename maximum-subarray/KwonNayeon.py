"""
Conditions:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Time Complexity: O(n)
- 배열을 한 번만 순회함

Space Complexity: O(1)
- 두 변수 이외에 추가 공간을 사용하지 않음

풀이방법: 
1. Base case: If nums is empty, return 0
2. Initialize variables (current_sum and max_sum as the first value in the array)
3. Traverse from the value at 1st index to the last, update current_sum
   - Decide whether to add the current value (num) to the existing subarray or start a new one
4. Update max_sum
   - Choose the larger between the updated current_sum and the previous max_sum
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(current_sum, max_sum)

        return max_sum
