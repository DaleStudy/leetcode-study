/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {    
    let result =  Array.from({length: nums.length}, () => 1) // Initialize return array

    // Iterate left to right
    let left = 1;
    for( let i =0 ; i<nums.length; i++ ) {
        result[i] *= left;
        left *= nums[i];
    }

    // Iterate right to left based on the result arr above
    let right = 1;
    for( let i=nums.length -1; i >=0; i-- ) {
        result[i] *= right;
        right *= nums[i];
    }

    // console.log(result)
    return result
};

/* 
    Time Complexity: O(n): Loop the nth nums array length
    Space Complexity: O(1)
*/



console.log(productExceptSelf([1,2,3,4])) 
console.log(productExceptSelf([-1,1,0,-3,3]))  


