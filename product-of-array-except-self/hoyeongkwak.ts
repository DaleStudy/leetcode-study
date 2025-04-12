/*
time complexity : O(n)
space complexity : O(1)
*/
function productExceptSelf(nums: number[]): number[] {
    const results = new Array(nums.length).fill(1) 
    let before = 1
    let after = 1
    for (let i = 0; i < nums.length - 1; i++) {
        before *= nums[i]
        results[i + 1] *= before
    }
    for (let i = nums.length - 1; i > 0; i--) {
        after *= nums[i]
        results[i - 1] *= after
    }

    return results
};