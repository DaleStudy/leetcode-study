/**
 * https://leetcode.com/problems/two-sum
 * time complexity : O(n)
 * space complexity : O(n)
 */
function twoSum(nums: number[], target: number): number[] {
    const m = new Map<number, number>();

    for (let i = 0; i < nums.length; i++) {
        if (m.has(nums[i]))
            return [m.get(nums[i]), i];
        m.set(target - nums[i], i);
    }

    return [-1, -1];
};
