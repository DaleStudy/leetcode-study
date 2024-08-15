// 시간복잡도: O(n)
// 공간복잡도: O(n)

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    return nums.length !== new Set(nums).size
};