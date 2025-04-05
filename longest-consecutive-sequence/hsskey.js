/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numSet = new Set(nums);
    let maxLength = 0;
    
    for (const num of nums) {
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let currentLength = 1;
            
            while (numSet.has(currentNum + 1)) {
                currentNum++;
                currentLength++;
            }
            maxLength = Math.max(maxLength, currentLength);
        }
    }
    
    return maxLength;
};
