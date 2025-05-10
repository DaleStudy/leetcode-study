/**
 * [Problem]: [300] Longest Increasing Subsequence
 * (https://leetcode.com/problems/longest-increasing-subsequence/)
 */

function lengthOfLIS(nums: number[]): number {
    //시간복잡도 O(n^2)
    //공간복잡도 O(n)
    function dpFunc(nums: number[]): number {
        const dp = new Array(nums.length + 1).fill(1);

        for (let i = 0; i < nums.length; i++) {
            for (let j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        return Math.max(...dp);
    }

    //시간복잡도 O(nlogn)
    //공간복잡도 O(n)
    function binearySearchFunc(nums: number[]): number {
        const results: number[] = [];

        for (const num of nums) {
            let left = 0;
            let right = results.length;

            while (left < right) {
                const mid = Math.floor((left + right) / 2);
                if (results[mid] < num) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            if (left < results.length) {
                results[left] = num;
            } else {
                results.push(num);
            }
        }

        return results.length;
    }

    return binearySearchFunc(nums);
}
