# TC : O(n)
# SC : O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # The sum of the numbers in the range(0,n)
        sumOfNums = (1 + n) * n // 2

        # Subtract every element of nums to leave only missing number
        for num in nums:
            sumOfNums -= num

        return sumOfNums
