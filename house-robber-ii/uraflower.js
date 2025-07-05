// 최대 금액은 ...
// nums[0]을 터는 경우:    rob(nums[2] ~ nums[last - 1]) + nums[0]
// nums[0]을 안 터는 경우:  rob(nums[1] ~ nums[last])
// 따라서 nums[0]을 털지 말지 여부를 기준으로 나누어 계산

/**
 * @param {number[]} nums
 * @return {number}
 */
const rob = function (nums) {
    if (nums.length === 1) return nums[0];

    const dp1 = [nums[0]]; // 첫 집을 터는 경우 최대 금액
    const dp2 = [0]; // 첫 집을 안 터는 경우 최대 금액

    for (let i = 1; i < nums.length; i++) {
        dp1[i] = Math.max(dp1[i - 1], (dp1[i - 2] || 0) + nums[i]);
        dp2[i] = Math.max(dp2[i - 1], (dp2[i - 2] || 0) + nums[i]);
    }

    return Math.max(dp1[dp1.length - 2], dp2[dp2.length - 1]);
}

// 시간복잡도: O(n)
// 공간복잡도: O(n)
