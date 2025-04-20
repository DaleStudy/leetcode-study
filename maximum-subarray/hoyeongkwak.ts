/* 
    time complexity : O(n)
    space complexity : O(1)
*/
function maxSubArray(nums: number[]): number {
    let maxSum = -Infinity
    let currSum = 0

    for (let i = 0; i < nums.length; i++) {
        currSum += nums[i]

        if (currSum > maxSum) {
            maxSum = currSum
        }

        if (currSum < 0) {
            currSum = 0
        }
    }
    return maxSum
};
