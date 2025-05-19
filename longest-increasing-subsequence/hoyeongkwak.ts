function lengthOfLIS(nums: number[]): number {
    let res = 1
    const dp: number[] = Array.from(nums).fill(1)
    for (let i = nums.length - 2; i >= 0; i--) {
        let curr = 1
        let j = i
        while(j < nums.length && curr < res + 1) {
            if (nums[j] > nums[i]) {
                curr = Math.max(curr, 1 + dp[j])
            }
            j++
        }
        dp[i] = curr
        res = Math.max(dp[i], res)
    }
    return res
};
