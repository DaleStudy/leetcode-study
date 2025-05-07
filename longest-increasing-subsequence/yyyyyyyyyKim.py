class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # DP(각 인덱스를 끝으로 하는 LIS의 최대 길이 저장)
        dp = [1]*len(nums)  # 초기값은 1(자신 하나만 있을 경우)

        for i in range(len(nums)):
            for j in range(i):
                # 현재값(nums[i])이 이전값(nums[j])보다 크면 dp[i]업데이트
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)

        # dp에 저장된 최대값 리턴
        return max(dp)

# 시간복잡도 O(n^2), 공간복잡도 O(n)
