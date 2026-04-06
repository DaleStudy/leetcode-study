class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        모르겠어서 풀이봤습니다 ㅜㅜ
        1.problem: 증가하는 가장 긴 subsequence length return (최장 증가 부분 수열)
        2.조건
        - nums array 길이 최소 1 , 최대 2500
        - 원소 값 음수 가능
        3.풀이
        - dp : time complexity O(n^2)
        dp[i] = i번째 원소를 마지막으로하는 LIS
        dp[i] max(dp[i], dp[j]+1) 나 보다 작은 애들 중 가장 긴 LIS + 1
        '''

        n = len(nums)
        dp = [1] * (n)
    
        for i in range(n):
            for j in range(i):
                 #앞 숫자 nums[j]가 지금 nums[i]보다 더 작은 경우 dp[i] update
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

       
        