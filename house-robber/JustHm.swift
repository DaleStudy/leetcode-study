class Solution {
    func rob(_ nums: [Int]) -> Int {
        guard nums.count != 1 else { return nums[0] }
        guard nums.count != 2 else { return max(nums[0], nums[1]) }
        
        // var dp = [nums[0], max(nums[0], nums[1])]
        var twoStepPrev = nums[0]
        var oneStepPrev = max(nums[0], nums[1])
        for i in 2..<nums.count {
            var maxNum = max(oneStepPrev, twoStepPrev + nums[i])
            twoStepPrev = oneStepPrev
            oneStepPrev = maxNum
            // var maxNum = max(dp[i-1], dp[i-2] + nums[i])
            // dp.append(maxNum)
        }
        // print(dp)
        // return dp.max() ?? 0
        return oneStepPrev
    }
}
