impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut dp = vec![0; nums.len() + 1];
        dp[1] = nums[0];
        for i in 2..dp.len() {
            dp[i] = dp[i - 1].max(dp[i - 2] + nums[i - 1]);
        }
        return *dp.last()
                .unwrap_or(&0)
    }
}
