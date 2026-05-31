/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {

    let n = nums.length + 1;
    let sortedNums = nums.sort((a, b) => a - b);

    for (let i = 0; i < n; i++) {
        if (sortedNums[i] === i) {
            continue;
        } else {
            return i;
        }
    }
};
