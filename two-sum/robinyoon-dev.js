/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    for (let i = 0; i < nums.length; i++) {
        let remaindedNum = target - nums[i];
        let matchedNum = nums.find((item) => remaindedNum === item);
        let matchedNumIndex = nums.indexOf(matchedNum, i + 1);
        // i와 matchedNumIndex 이 같은 숫자면 안 됨.
        if (i === matchedNumIndex) {
            continue;
        } else if (matchedNumIndex === -1) {
            continue;
        }
        else {
            return [i, matchedNumIndex];
        }
    }
};
