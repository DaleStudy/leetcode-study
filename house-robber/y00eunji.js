/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const len = nums.length;
    if (len === 0) return 0;
    if (len === 1) return nums[0];
    if (len === 2) return Math.max(nums[0], nums[1]);

    const dp = Array(len).fill(0);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);

    // 현재 집을 터는 경우와 안 터는 경우 중 최대값 선택
    // 1. 이전 집까지의 최대 금액 (현재 집 스킵)
    // 2. 전전 집까지의 최대 금액 + 현재 집 금액 (현재 집 선택)
    for (let i = 2; i < len; i++) {
        dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
    }

    return dp[len - 1];
};
