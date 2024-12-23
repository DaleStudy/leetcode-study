/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


// Time Complexity : O(n)
// Space Complexity : O(n)

var twoSum = function (nums, target) {

    let map = new Map();

    for (let i = 0; i < nums.length; i++) {

        const temp = target - nums[i];

        if (map.has(temp)) {
            return [i, map.get(temp)]
        }

        map.set(nums[i], i);
    }

    return [];
}


// Time Complexity: O(n^2)
// Space Complexity: O(1)
// This solution is straightforward but inefficient for large arrays. For better performance, consider the hashmap approach.

// var twoSum = function (nums, target) {

//     for (let i = 0; i < nums.length; i++) {

//         const loc = nums.indexOf((target - nums[i]), i + 1);

//         if (loc >= 0) {
//             return [i, loc]
//         } else {
//             continue;
//         }

//     }

// };

