/**
 * https://leetcode.com/problems/missing-number
 * time complexity : O(n)
 * space complexity : O(n)
 */
function missingNumber(nums: number[]): number {
    const set = new Set<number>(nums);

    for (let i = 0; i < set.size + 1; i++) if (!set.has(i)) return i;

    return 0;
};
