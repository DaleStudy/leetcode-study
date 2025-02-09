/**
 * @param {number[]} nums
 * @return {number}
 */

// Dynamic programming


// Optimized Solution:
// Time Complexity: O(n)
// Space Complexity: O(1)


var maxSubArray = function (nums) {

    let currentMax = nums[0];
    let globalMax = nums[0]

    for (let i = 1; i < nums.length; i++) {

        currentMax = Math.max(currentMax + nums[i], nums[i]);
        globalMax = Math.max(currentMax, globalMax);

    }

    return globalMax;

};


// Time Complexity: O(n)
// Space Complexity: O(n)

// var maxSubArray = function (nums) {

//     let dp = [nums[0]];

//     for (let i = 1; i < nums.length; i++) {

//         dp[i] = Math.max(dp[i - 1] + nums[i], nums[i])

//     }

//     return Math.max(...dp)

// };


