/**
 *
 * @param {number[]} nums
 * @param nums
 *
 * 풀이
 * dp 배열을 사용해 nums 배열의 길이만큼 초기화한다.
 * dp[0]은 nums[0]으로 초기화하고, dp[1]은 nums[0]과 nums[1] 중 큰 값으로 초기화한다.
 * dp[2]부터는 dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i])로 초기화한다.
 * dp[i-1]은 i번째 집을 털지 않은 경우, dp[i-2] + nums[i]는 i번째 집을 털고 i-1번째 집을 털지 않은 경우이다.
 *
 */

function rob(nums: number[]): number {
    const n = nums.length
    if(n===0) return 0
    if(n===1) return nums[0];

    let dp0 = nums[0]
    let dp1 = Math.max(nums[0], nums[1]);

    for(let i=2;i<n;i++){
        const curMaxValue = Math.max(dp1, dp0 + nums[i]);
        dp0 = dp1;
        dp1 = curMaxValue;
    }

    return dp1
};
