/**
 * https://leetcode.com/problems/contains-duplicate
 * time complexity : O(n)
 * space complexity : O(n)
 */

export function containsDuplicate(nums: number[]): boolean {
    const seen = new Set<number>();
    for (const num of nums) {
        if (seen.has(num)) {
            return true;
        }
        seen.add(num);
    }
    return false;
};