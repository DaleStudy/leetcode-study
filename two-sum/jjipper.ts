/**
 * https://leetcode.com/problems/two-sum
 * time complexity : O(n)
 * space complexity : O(n)
 */

export function twoSum(nums: number[], target: number): number[] {
    const obj: Record<number, number> = {};
    for (let i = 0; i < nums.length; i++) {
        const a = nums[i];
        const b = target - a;
        if (b in obj) {
            return [obj[b], i];
        }
        obj[a] = i;
    }
    return [];
};
