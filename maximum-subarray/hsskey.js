/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSum = -Infinity
    let currentSum = 0

    for(let num of nums) {
        currentSum = Math.max(num, currentSum + num)
        maxSum = Math.max(maxSum, currentSum)
    }

    return maxSum
};
