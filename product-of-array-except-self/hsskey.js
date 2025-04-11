/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const n = nums.length
    const result = Array(nums.length)

    let left = 1

    for(let i = 0; i < n; i++) {
        result[i] = left
        left *= nums[i]
    }

    let right = 1
    for(let i = n - 1; i >= 0; i--) {
        result[i] *= right
        right *= nums[i]
    }

    return result
};
