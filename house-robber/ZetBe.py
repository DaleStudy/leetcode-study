'''
문제: 연속한 집이 아닌 집을 털 때 얻을 수 있는 최대 금액을 구하는 문제
풀이: 다이나믹 프로그래밍
    초기 값 설정 후,
    dp[i] = max(dp[i-2], dp[i-3]) + nums[i] 점화식 설정
    한집, 혹은 두집을 건너서 털었을 경우, 둘 중 가장 큰값을 고름

시간복잡도: O(n)
    점점 순차적으로 dp 배열을 채워나가므로 O(n)
공간복잡도: O(n)
    dp 배열을 하나 생성하므로 O(n)

사용한 자료구조: 리스트

'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0], nums[1], nums[0]+nums[2])

        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0]+nums[2]

        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        return max(dp[len(nums)-1], dp[len(nums)-2])
    
    