/**
 * https://leetcode.com/problems/product-of-array-except-self
 * time complexity : O(n)
 * space complexity : O(1)
 */
function productExceptSelf(nums: number[]): number[] {
    const n = nums.length;
    const answer = new Array(n).fill(1);

    let leftProduct = 1;
    for (let i = 0; i < n; i++) {
        answer[i] = leftProduct;
        leftProduct *= nums[i];
    }

    let rightProduct = 1;
    for (let i = n - 1; i >= 0; i--) {
        answer[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return answer;
}
