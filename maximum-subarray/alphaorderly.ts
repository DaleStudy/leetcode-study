function maxSubArray(nums: number[]): number {
    let ans = nums[0]
    let sub = nums[0]

    for (let i = 1;i < nums.length;i += 1) {
        sub = Math.max(sub + nums[i], nums[i])
        ans = Math.max(ans, sub)
    }

    return ans
};
