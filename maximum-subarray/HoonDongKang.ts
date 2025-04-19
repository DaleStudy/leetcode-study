/**
 * [Problem]: [53] Maximum Subarray
 *
 * (https://leetcode.com/problems/maximum-subarray/description/)
 */

function maxSubArray(nums: number[]): number {
    //시간복잡도 O(n)
    //공간복잡도 O(1)
    function getMax(nums: number[]): number {
        let result = nums[0];
        let sum = 0;

        nums.forEach((num) => {
            sum = Math.max(num, sum + num);
            result = Math.max(sum, result);
        });

        return result;
    }

    //시간복잡도 O(n)
    //공간복잡도 O(1)
    function dpFunc(nums: number[]): number {
        const dp = Array(nums.length).fill(0);
        dp[0] = nums[0];

        for (let i = 1; i < nums.length; i++) {
            dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
        }

        return Math.max(...dp);
    }

    return dpFunc(nums);
}
