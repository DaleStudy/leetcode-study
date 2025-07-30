class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return max(dp)

'''
시간 복잡도: O(n log n)
- set() -> O(n)
- sorted() -> O(n log n)
- for loop -> O(n)
- max() -> O(n)

공간 복잡도: O(n)
- set() -> O(n)
- sorted list -> O(n)
- rs -> O(n)
- O(3n) => O(n)
'''
