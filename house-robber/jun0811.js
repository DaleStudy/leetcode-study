/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const n = nums.length;
    if (n === 1) return nums[0];    
    if (n === 2) return Math.max(nums[0], nums[1]);
    const dp = [nums[0],nums[1],nums[2] + nums[0]];
    
    for(let i =3; i < n; i++) {
        const tmp1 = dp[i-2] + nums[i]
        const tmp2 = dp[i-3] + nums[i]
        dp[i] = tmp1> tmp2 ? tmp1 : tmp2
    }
    return dp[n-1] > dp[n-2] ? dp[n-1] : dp[n-2]
};
