/**
 * Runtime: 17ms, Memory: 63.18MB
 * 
 * Time Complexity: O(n)
 *  - Array to Set takes O(n)
 *  - Compare Set size and array length takes O(1)
 * Space Complexity: O(n)
 *  - Space for Set : O(n)
*/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    return new Set(nums).size !== nums.length
};
