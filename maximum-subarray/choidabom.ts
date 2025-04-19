// https://leetcode.com/problems/maximum-subarray/

// Time Limit Exceeded
function maxSubArray(nums: number[]): number {
    const acc = []
    const len = nums.length

    for (let size = 1; size <= len; size++) {
        for (let start = 0; start <= len - size; start++) {
            const sub = nums.slice(start, start + size)
            const sum = sub.reduce((acc, num)=> acc += num, 0)
            acc.push(sum)
        }
    }

    return acc.sort((a, b) => b - a)[0]
};

// TC: O(n) 
// SC: O(n)  

function maxSubArray(nums: number[]): number {
    const dp = [...nums]; 
    let max = dp[0];

    for (let i = 1; i < nums.length; i++) {
        dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
        max = Math.max(max, dp[i]);
    }

    return max;
}
