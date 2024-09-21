/**
 * https://leetcode.com/problems/longest-increasing-subsequence
 * time complexity : O(n)
 * space complexity : O(n)
 */
function lengthOfLIS(nums: number[]): number {
    const [head] = nums;
    const basket = [head];

    for (let i = 1; i < nums.length; i++) {
        const current = nums[i];
        let j = 0;

        while (j < basket.length && basket[j] < current) j++;

        if (j === basket.length) basket.push(current);
        else basket[j] = current;
    }

    return basket.length;
};
