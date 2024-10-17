// 시간복잡도: O(n)
// 공간복잡도: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
    let maxNum = -Infinity;
    let prevSum = -Infinity;

    for (let i = 0 ; i < nums.length; i++) {
        prevSum = Math.max(prevSum + nums[i], nums[i])
        maxNum = Math.max(prevSum, maxNum)
    }


    return maxNum
};
