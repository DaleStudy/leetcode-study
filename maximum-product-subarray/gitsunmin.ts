/**
 * https://leetcode.com/problems/maximum-product-subarray
 * time complexity : O(n)
 * space complexity : O(1)
 */
function maxProduct(nums: number[]): number {
    let r = nums[0];
    let mx = 1, mn = 1;

    for (let i = 0; i < nums.length; i++) {
        const tempMx = mx * nums[i];
        const tempMn = mn * nums[i];

        mx = Math.max(tempMx, tempMn, nums[i]);
        mn = Math.min(tempMx, tempMn, nums[i]);

        r = Math.max(r, mx);
    }

    return r;
}
