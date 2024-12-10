/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let dup_set = new Set(); // Initialize Set
    for (let num of nums) {
        dup_set.add(num) // Add value into the set (duplicated value will be ignored)
    }

    if(dup_set.size !== nums.length) {
        return true
    }
    return false
};

/* 
    Space Complexity - O(n) - Create a set to store elements
    Time Complexity - O(n) - Traverse through the array
*/


/* Test code */
console.log(containsDuplicate([1, 2, 3, 1])); // true
console.log(containsDuplicate([1, 2, 3, 4])); // false
console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])); // true


