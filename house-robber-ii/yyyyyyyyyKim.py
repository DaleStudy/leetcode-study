class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # DP
        # 시간복잡도 O(n^2), 공간복잡도 O(n)

        # 집이 1개~3개인 경우, 가장 큰 집만 털기
        if len(nums) <= 3:
            return max(nums)

        # 첫 번째 집을 포함하지 않고 털기
        dp1 = [0]*len(nums)
        dp1[1] = nums[1]
        dp1[2] = nums[2]
        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i-1], max(dp1[:i-1])+nums[i])

        # 마지막 집을 포함하지 않고 털기
        dp2 = [0]*len(nums)
        dp2[0] = nums[0]
        dp2[1] = nums[1]
        for i in range(2, len(nums)-1):
            dp2[i] = max(dp2[i-1], max(dp2[:i-1])+nums[i])

        return max(max(dp1), max(dp2))
