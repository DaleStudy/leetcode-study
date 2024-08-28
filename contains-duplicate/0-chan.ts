/**
 * time complexity : O(n)
 * space complexity : O(n)
 */
function containsDuplicate(nums: number[]): boolean {
    const hasDuplicate = new Set(nums).size !== nums.length;
    return hasDuplicate;
};
