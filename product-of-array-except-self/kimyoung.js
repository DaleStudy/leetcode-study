var productExceptSelf = function (nums) {
    let result = new Array(nums.length).fill(0); // create a result array of length num
    let pre = 1, post = 1; // default to 1 

    for (let i = 0; i < nums.length; i++) { // fill the result array with prefix (multiplication of left values)
        result[i] = pre;
        pre *= nums[i];
    }
    for (let i = nums.length - 1; i >= 0; i--) { // multiply the postfix (multiplication of right values) to the result array in their corresponding index
        result[i] *= post;
        post *= nums[i];
    }

    return result;
};

// time - O(n) iterate through the nums array twice - 2n, remove constant which ends up to be n
// space - O(1) result array not part of space complexity
