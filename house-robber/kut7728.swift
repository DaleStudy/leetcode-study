class Solution {
    func rob(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        if n == 1 { return nums[0] }
        if n == 2 { return max(nums[0], nums[1]) }

        //dp[i]는 i번까지 고려했을 때 가능한 최대 금액
        var dp = [Int](repeating: 0, count: n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  //첫째 or 둘째 집 중 더 비싼 집 털기

        //각 dp의 자리에는 바로 전 값을 그대로 가져오거나(i를 안털기), 전전집까지 턴거+i턴 값 중에서 비싼쪽 저장
        for i in 2..<n {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        }

        //마지막 집까지 고려한 최대 이익 반환하기
        return dp[n - 1]
    }
}
