/**
 * https://leetcode.com/problems/house-robber/
 * time complexity : O(n)
 * space complexity : O(n)
 */

function rob(nums: number[]): number {
    const houseCount = nums.length;

    if (houseCount === 0) return 0;
    if (houseCount === 1) return nums[0];

    const maxRobAmount = new Array(houseCount).fill(0);
    maxRobAmount[0] = nums[0];
    maxRobAmount[1] = Math.max(nums[0], nums[1]);

    for (let i = 2; i < houseCount; i++) maxRobAmount[i] = Math.max(maxRobAmount[i - 1], maxRobAmount[i - 2] + nums[i]);

    return maxRobAmount[houseCount - 1];
};
