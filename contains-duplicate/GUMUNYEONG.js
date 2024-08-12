/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
    const setObj = new Set(nums);

    const diff = !(nums.length === setObj.size);

    return diff;
};

// TC: O(n)
// SC: O(n)