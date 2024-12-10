/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    // set에 넣어 중복을 줄이고 길이를 비교한다.

    return new Set(nums).size !== nums.length;
};
