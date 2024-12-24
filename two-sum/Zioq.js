/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Initialize object to save remained value with index
    let remain_with_index_obj = {}

    for ( let i =0; i<nums.length++; i++ ) {
        let remain = target - nums[i]; // Calculate reamined value to check 

        // If remained value found in the object, return current index and object's key
        if( remain_with_index_obj.hasOwnProperty(remain) ) {
            return [i, remain_with_index_obj[remain]]
        }

        // Save the valu as key
        remain_with_index_obj[nums[i]] = i;
    }
    return null
};

/* 
    Time Complexity: O(n)
    Space Complexity: O(n)
*/

console.log(twoSum([2,7,11,15], 9));
console.log(twoSum([3,2,4], 6));
