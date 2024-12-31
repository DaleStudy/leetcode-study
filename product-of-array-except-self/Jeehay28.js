/**
 * @param {number[]} nums
 * @return {number[]}
 */

// Time Complexity: O(n)
// Space Complexity: O(n)
var productExceptSelf = function (nums) {

    let result = [];

    let left = Array(nums.length).fill(1)
    let right = Array(nums.length).fill(1)

    for (let i = 1; i < nums.length; i++) {

        left[i] = left[i - 1] * nums[i - 1];
        right[nums.length - 1 - i] = right[right.length - i] * nums[nums.length - i]

    }

    for (let i = 0; i < nums.length; i++) {
        result[i] = left[i] * right[i];
    }

    return result;


};

