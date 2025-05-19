/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    const dp = new Array(nums.length).fill(1);

    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i] && dp[j] >= dp[i]) {
                dp[i] = dp[j] + 1;
            }
        }
    }

    return Math.max(...dp);
};

// 시간 복잡도 : O(n^2)
// 공간 복잡도 : O(n)
