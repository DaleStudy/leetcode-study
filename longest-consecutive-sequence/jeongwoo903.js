/**
 * @param {number[]} nums
 * @return {number}
 */

var longestConsecutive = function(nums) {
    if (nums.length <= 1) return nums.length;

    const sortedArray = [...new Set(nums)].sort((a,b) => a - b);

    let maxLength = 1;
    let currentLength = 1;

    for (let i = 1; i < sortedArray.length; i++) {
        if (sortedArray[i] === sortedArray[i-1] + 1) {
            currentLength++;
        } else {
            currentLength = 1;
        }

        maxLength = Math.max(maxLength, currentLength);
    }

    return maxLength;
};
