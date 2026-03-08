/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {

    const NUMS_LENGTH = nums.length;

    if (NUMS_LENGTH === 0) return 0;
    if (NUMS_LENGTH === 1) return nums[0];

    const maxSumsArr = new Array(NUMS_LENGTH);
    maxSumsArr[0] = nums[0];
    maxSumsArr[1] = Math.max(nums[0], nums[1]);

    for (let i = 2; i < NUMS_LENGTH; i++) {
        maxSumsArr[i] = Math.max(maxSumsArr[i - 2] + nums[i], maxSumsArr[i - 1]);
    }

    return maxSumsArr[NUMS_LENGTH - 1];

};
