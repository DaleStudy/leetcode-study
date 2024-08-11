/**
 * https://leetcode.com/problems/contains-duplicate/
 * time complexity : O(n)
 * space complexity : O(n)
 */
function containsDuplicate(nums: number[]): boolean {
    return new Set(nums).size !== nums.length
};