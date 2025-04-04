/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numSet = new Set(nums);

    let maxLength = 0;
    let currentLength = 0;

    nums.forEach(num => {
        let currentNum = num;
        while(numSet.has(currentNum)) {
            numSet.delete(currentNum)
            currentNum += 1;
            currentLength += 1;
        }

        currentNum = num - 1;
        while(numSet.has(currentNum)) {
            numSet.delete(currentNum)
            currentNum -= 1;
            currentLength += 1;
        }

        maxLength = Math.max(maxLength, currentLength);
        currentLength = 0;
    });

    return maxLength;
};
