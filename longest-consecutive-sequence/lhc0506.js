/**
 * @param {number[]} nums
 * @return {number}
 */

var longestConsecutive = function(nums) {
    const numSet = new Set(nums);

    let maxLength = 0;
    let currentLength = 0;

    const countConsecutive = (num, step) => {
        let currentNum = num;
        while(numSet.has(currentNum)) {
            numSet.delete(currentNum);
            currentNum += step;
            currentLength += 1;
        }
    }

    nums.forEach(num => {
        countConsecutive(num, 1);
        countConsecutive(num - 1, -1);

        maxLength = Math.max(maxLength, currentLength);
        currentLength = 0;
    });

    return maxLength;
};
