class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))  # 처음에는 nums.sort()로 풀었지만
        # elif문에 중복 처리 부분을 넣어야해서 set으로 중복 허용 x
        k=len(nums)

        # Space: O(n), Time: O(n log n) - 정렬 O(n log n) + DP  O(n)
        dp=[1 for _ in range(k)] # dp[i] = nums[i]로 끝나는 연속 수열의 길이
        for i in range(1,k):
            if nums[i]-nums[i-1]==1:
                dp[i]=dp[i-1]+1
        return max(dp)
        
